from django.urls import path
from . import views

urlpatterns = [
    path('', views.apple, name= 'apple'),
]