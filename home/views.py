from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse

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
    return render(request,'contact.html')
