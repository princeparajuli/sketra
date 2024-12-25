
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('houseplan/', views.houseplan, name='houseplan'),
    path('registerpg/', views.registerpg, name='registerpg'),
    
]
