from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import contact

# Create your views here.
def index(request):
    context = {
        'my_name' : "Tauqeer Ahmad"
    }
    return render(request,'index.html',context)
    # returm HttpResponse("this is homepage.")

def services(request):
    return render(request,'services.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        Contact = contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today() )
        Contact.save()
    return render(request,'contact.html')
