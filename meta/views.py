from django.shortcuts import render

# Create your views here.
def Menu(request):
    return render(request, 'meta/meta.html')

from .forms import CustomerForm
# link from forms.py
def customer_forms(request):
    form = CustomerForm()

    return render(request, 'meta/forms.html', {'form': form})