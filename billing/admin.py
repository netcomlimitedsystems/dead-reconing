from django.contrib import admin
from .models import Enterprise, EnterpriseUser, Plan, Voucher, Transaction

@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'contact_phone', 'is_verified', 'created_at')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name', 'contact_email', 'contact_phone')
    list_filter = ('is_verified',)

@admin.register(EnterpriseUser)
class EnterpriseUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'enterprise', 'is_admin')
    search_fields = ('user__username', 'enterprise__name')

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'enterprise', 'price', 'duration_value', 'duration_unit', 'created_at')
    list_filter = ('enterprise',)
    search_fields = ('name',)

@admin.register(Voucher)
class VoucherAdmin(admin.ModelAdmin):
    list_display = ('code', 'plan', 'enterprise', 'is_redeemed', 'redeemed_at', 'created_at')
    list_filter = ('enterprise', 'is_redeemed')
    search_fields = ('code', 'plan__name', 'enterprise__name')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('external_id', 'enterprise', 'amount', 'phone', 'status', 'created_at')
    list_filter = ('enterprise', 'status')
    search_fields = ('external_id', 'phone', 'enterprise__name')
