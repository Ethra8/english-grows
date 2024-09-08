from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.company_service, name='company_service'),
]
