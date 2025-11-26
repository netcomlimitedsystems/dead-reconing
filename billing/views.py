from django.shortcuts import render, redirect
from .forms import EnterpriseRegisterForm
from django.contrib import messages

def enterprise_register(request):
    if request.method == 'POST':
        form = EnterpriseRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            ent = form.save(commit=False)
            ent.is_verified = False  # Await manual verification
            ent.save()
            messages.success(request, "Enterprise registered successfully! Await verification.")
            return redirect('billing_index')
    else:
        form = EnterpriseRegisterForm()
    return render(request, 'billing/enterprise_register.html', {'form': form})

from django.http import HttpResponse

def index(request):
    return HttpResponse("Billing app is working!")
