from django.contrib import admin
from django.urls import path
from . import views
from company_services.views import company_service

urlpatterns = [
    path('', views.index, name='home'),
    path('company_services/', views.companies, name='company_services'),
]
