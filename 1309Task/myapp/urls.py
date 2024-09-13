from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.showfirst),
    path('second',views.showsecond),
    path('third',views.showthird),
    path('first',views.showfirst1),
    path('fourth',views.showfourth),
    path('five',views.showfifth),
    path('sixth',views.showsixth),
    path('seven',views.showseven),
    path('eight',views.showeight),
    path('nine',views.shownine),
    path('ten',views.showten)
]