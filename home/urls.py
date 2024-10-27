from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('companies/', views.companies, name='companies'),
    path('about/', views.about, name='about'),
]
