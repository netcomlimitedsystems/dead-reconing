import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone

User = settings.AUTH_USER_MODEL

# Duration units for plans
DURATION_UNITS = (
    ("hours", "Hours"),
    ("days", "Days"),
    ("weeks", "Weeks"),
    ("months", "Months"),
)

class Enterprise(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=30)
    address = models.TextField(blank=True)
    vat_number = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(upload_to='enterprise_logos/', blank=True, null=True)
    documents = models.FileField(upload_to='enterprise_docs/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class EnterpriseUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, related_name='users')
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} ({self.enterprise.name})"


class Plan(models.Model):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, related_name='plans')
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_value = models.PositiveIntegerField()  # e.g., 1, 7, 30
    duration_unit = models.CharField(max_length=10, choices=DURATION_UNITS)
    data_quota_mb = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.enterprise.name})"


class Voucher(models.Model):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    code = models.CharField(max_length=64, unique=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    username = models.CharField(max_length=64, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    is_redeemed = models.BooleanField(default=False)
    redeemed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.plan.name}"


class Transaction(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    )

    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    external_id = models.CharField(max_length=200)  # e.g., M-Pesa checkout ID
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=30)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    meta = models.JSONField(default=dict, blank=True)  # store raw callback data

    def __str__(self):
        return f"{self.external_id} - {self.status}"
