from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DonorRegForm
from .models import BloodDonor
from stocks.models import BloodStock

# Create your views here.

def blood_stock(request):
    blood_stock = BloodStock.objects.all()
    donors = BloodDonor.objects.all()
    groups = {}
    for donor in donors :
        if donor.blood_group in groups.keys():
            groups[donor.blood_group] += 1
        else:
            groups[donor.blood_group] = 1

    
    return render(request,"bloodbank/blood_stock.html", context={'stock':blood_stock, 'groups': groups})

def bloodbank_about(request):
    return render(request,"bloodbank/bloodbank_about.html")

def donor_reg(request):
    form = DonorRegForm()
    if request.method == "POST":
        form = DonorRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        "form": form
    }
    return render(request,"bloodbank/donor_reg.html", context)

