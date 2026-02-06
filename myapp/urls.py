from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('myprofile/', views.myprofile, name='myprofile'),
]
