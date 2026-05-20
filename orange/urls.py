from django.urls import path
from . import views

urlpatterns = [
    path('', views.orange, name= 'orange'),
]