from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.showhomepage),
    path('contact',views.showcontact,name = 'contact'),
    path('product',views.showproduct)
]