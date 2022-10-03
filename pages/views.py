from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from .models import Plumbing, Painting , Tilesfix , Electrical , Furniture, Accodition
from django.contrib import messages
from django.http import HttpResponseRedirect



# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def maintenance(request):
    return render(request, 'pages/maintenance.html')

def accodition(request):
    
    return render(request, 'pages/accodition.html')

def furniture(request):
    return render(request, 'pages/furniture.html')


def plumbing(request):
    # submitted = False
    
    if request.method == 'POST':
        # messages.error(request, 'This is error message')
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        flat_no = request.POST['flat_no']
        building_names = request.POST['building_names']
        type_of_services = request.POST['type_of_services']
        date = request.POST['date']
        message = request.POST['message']
        purpose = request.POST['purposes']
        
       
        form = Plumbing(full_name=full_name,phone=phone,flat_no=flat_no,building_names=building_names,type_of_services=type_of_services,date=date,message=message,purpose=purpose)
        form.save()
        messages.success(request, 'Your request has been submitted successfully')
               
    return render(request, 'pages/plumbing.html')

def plumbing(request):
    # submitted = False
    
    if request.method == 'POST':
        # messages.error(request, 'This is error message')
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        flat_no = request.POST['flat_no']
        building_names = request.POST['building_names']
        type_of_services = request.POST['type_of_services']
        date = request.POST['date']
        message = request.POST['message']
        purpose = request.POST['purposes']
        
       
        form = Plumbing(full_name=full_name,phone=phone,flat_no=flat_no,building_names=building_names,type_of_services=type_of_services,date=date,message=message,purpose=purpose)
        form.save()
        messages.success(request, 'Your request has been submitted successfully')
               
    return render(request, 'pages/plumbing.html')

def accodition(request):
    # submitted = False
    
    if request.method == 'POST':
        # messages.error(request, 'This is error message')
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        flat_no = request.POST['flat_no']
        building_names = request.POST['building_names']
        type_of_services = request.POST['type_of_services']
        date = request.POST['date']
        message = request.POST['message']
        purpose = request.POST['purposes']
        
       
        form = Accodition(full_name=full_name,phone=phone,flat_no=flat_no,building_names=building_names,type_of_services=type_of_services,date=date,message=message,purpose=purpose)
        form.save()
        messages.success(request, 'Your request has been submitted successfully')
               
    return render(request, 'pages/painting.html')
   
    # form = PlumbingForm(request.POST)
    # if form.is_valid():
    #     form.save()
    # return render(request, 'pages/plumbing.html', {'form': form})

def tilesfix(request):
    
    if request.method == 'POST':
        # messages.error(request, 'This is error message')
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        flat_no = request.POST['flat_no']
        building_names = request.POST['building_names']
        type_of_services = request.POST['type_of_services']
        date = request.POST['date']
        message = request.POST['message']
        purpose = request.POST['purposes']
        
       
        form = Tilesfix(full_name=full_name,phone=phone,flat_no=flat_no,building_names=building_names,type_of_services=type_of_services,date=date,message=message,purpose=purpose)
        form.save()
        messages.success(request, 'Your request has been submitted successfully')
               
    return render(request, 'pages/tilesfix.html')
    

def contact(request):
    return render(request, 'pages/contact.html')

def electrical(request):
    
    if request.method == 'POST':
        # messages.error(request, 'This is error message')
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        flat_no = request.POST['flat_no']
        building_names = request.POST['building_names']
        type_of_services = request.POST['type_of_services']
        date = request.POST['date']
        message = request.POST['message']
        purpose = request.POST['purposes']
        
       
        form = Electrical(full_name=full_name,phone=phone,flat_no=flat_no,building_names=building_names,type_of_services=type_of_services,date=date,message=message,purpose=purpose)
        form.save()
        messages.success(request, 'Your request has been submitted successfully')
    return render(request, 'pages/electrical.html')


def furniture(request):
    
    if request.method == 'POST':
        # messages.error(request, 'This is error message')
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        flat_no = request.POST['flat_no']
        building_names = request.POST['building_names']
        type_of_services = request.POST['type_of_services']
        date = request.POST['date']
        message = request.POST['message']
        purpose = request.POST['purposes']
        
       
        form = Furniture(full_name=full_name,phone=phone,flat_no=flat_no,building_names=building_names,type_of_services=type_of_services,date=date,message=message,purpose=purpose)
        form.save()
        messages.success(request, 'Your request has been submitted successfully')
    
    return render(request, 'pages/electrical.html')


def painting(request):   
    if request.method == 'POST':
        # messages.error(request, 'This is error message')
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        flat_no = request.POST['flat_no']
        building_names = request.POST['building_names']
        type_of_services = request.POST['type_of_services']
        date = request.POST['date']
        message = request.POST['message']
        purpose = request.POST['purposes']
        
        form = Painting(full_name=full_name,phone=phone,flat_no=flat_no,building_names=building_names,type_of_services=type_of_services,date=date,message=message,purpose=purpose)
        form.save()
        messages.success(request, 'Your request has been submitted successfully')
    
    return render(request, 'pages/electrical.html')

def ourservices1(request):
    return render(request, 'pages/ourservices1.html')

def ourservices2(request):
    return render(request, 'pages/ourservices2.html')
