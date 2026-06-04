from django.urls import path
from . import views

urlpatterns = [
    path('', views.orange, name= 'orange'),
    path('home/', views.form_view, name= 'home')
]