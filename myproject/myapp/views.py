from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(req):
    emp = Employee.objects.all()
    context = {
        'emp': emp
    }
    return render(req, 'index.html', context)

def add(req):
    if req.method=='POST':
        name = req.POST.get('name')
        email=req.POST.get('email')
        address = req.POST.get('address')
        phone = req.POST.get('phone')

        emp = Employee(
            name=name,
            email=email,
            address=address,
            phone=phone
        )

        emp.save()
        return redirect("home")
    return render(req, 'index.html')

def edit(req):
    emp = Employee.objects.all()
    context = {
        'emp': emp
    }
    return redirect(req, 'index.html', context)

def update(req, id):
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        address = req.POST.get('address')
        phone = req.POST.get('phone')

        emp = Employee(
            id=id,
            name=name,
            email=email,
            address = address,
            phone = phone
        )
        emp.save()
        return redirect("home")
    return redirect(req, 'index.html')

def delete(req, id):
    emp = Employee.objects.filter(id=id)
    emp.delete()
    context = {
        'emp': emp
    }
    return redirect("home")