from django.shortcuts import render

# Create your views here.
def Menu(request):
    return render(request, 'meta/meta.html')