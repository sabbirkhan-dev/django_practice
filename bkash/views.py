from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Pay_Method

def bkash(request):
    return HttpResponse("This is a bkash page")


def home(request):
    return render(request, 'bkash/home.html')


def payment_method(request):
    pay_m = Pay_Method.objects.all()
    return render(request, 'bkash/pay.html', {'pay' : pay_m})

from .forms import RecentProduct
# link from forms.py
def details(request):
    frm = RecentProduct(auto_id=True, label_suffix=" - ")
    return render(request, 'bkash/recent.html', {'form': frm})