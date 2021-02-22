from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('reg/', views.reg, name='reg'), #http://127.0.0.1:8000/data/reg
    path('catalog/', views.get_catalog, name='catalog'),
    path('log_in/', views.log_in, name='login'),
]
