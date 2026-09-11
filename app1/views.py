from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio_app1(request):
    return HttpResponse('Bienvenido a App 1 - Inicio') 

def contacto_app1(request):
    return HttpResponse('App 1 - Página de Contacto')