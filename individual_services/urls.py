from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.individual_services, name= 'individual_services'),
]
