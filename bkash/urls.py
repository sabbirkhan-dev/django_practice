from django.urls import path
from . import views

urlpatterns = [
    path('', views.bkash, name= 'bkash'),
    path('home/', views.home, name= 'home'),
    path('pay/', views.payment_method, name= 'pay'),
]