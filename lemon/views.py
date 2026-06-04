from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
# def bkash(request):
#     return HttpResponse("This is a bkash page")

from .forms import LogForm
def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    contex = {'form' : form}
    return render(request, 'lemon_home.html', contex)
