from django.contrib import admin
from django.urls import path

def desdeapps(self):
    print('--------------------------Desde app dependencia -------------')

urlpatterns = [
    path('dependencia/', desdeapps),
]