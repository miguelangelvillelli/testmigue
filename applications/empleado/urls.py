from django.contrib import admin
from django.urls import path

def desdeapps(self):
    print('--------------------------Desde app empleado -------------')

urlpatterns = [
    path('empleado/', desdeapps),
]