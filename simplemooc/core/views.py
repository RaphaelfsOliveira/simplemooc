from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def base(request):
    return render(request, 'base_core.html')

def home(request):
    return render(request, 'home_core.html')

def contact(request):
    return render(request, 'contact.html')
