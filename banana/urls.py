from django.urls import path
from . import views

urlpatterns = [
    path('', views.banana, name= 'banana'),
]