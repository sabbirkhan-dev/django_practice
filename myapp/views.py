from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'myapp/index.html')

def sabbir(request):
    return HttpResponse("Hello sabbir function")
