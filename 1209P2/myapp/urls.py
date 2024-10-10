from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.showindex),
    path('contact',views.showcontact)
]
