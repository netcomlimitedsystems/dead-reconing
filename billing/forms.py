from django import forms
from .models import Enterprise

class EnterpriseRegisterForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = [
            'name', 'slug', 'contact_email', 'contact_phone',
            'address', 'vat_number', 'logo', 'documents'
        ]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }
