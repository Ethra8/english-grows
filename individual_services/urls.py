from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.individual_services, name= 'individual_services'),
    path('<int:service_id>/', views.pack_details, name= 'pack_details'),
]
