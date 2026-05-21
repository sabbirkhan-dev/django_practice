from django.urls import path
from . import views

urlpatterns = [
    path('', views.Menu, name='meta'),
    path('forms/', views.customer_forms, name='forms'),
]
