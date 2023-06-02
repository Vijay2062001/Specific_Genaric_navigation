from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def mam(request):
    return render(request,'mam.html')

def sravani(request):
    return HttpResponse('My second Mother')

    
