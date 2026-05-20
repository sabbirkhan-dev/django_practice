from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bkash(request):
    return HttpResponse("This is a bkash page")
