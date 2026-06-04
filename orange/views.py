from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def orange(request):
    return HttpResponse("This is a orange page")

from .forms import InputForms
def form_view(request):
    form = InputForms()
    context = {'form': form}
    return render(request, 'home.html', context)