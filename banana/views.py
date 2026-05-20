from django.shortcuts import render

# Create your views here.

def banana(request):
    return render(request, "banana/banana.html")