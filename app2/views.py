from django.shortcuts import render
from django.http import HttpResponse

def inicio_app2(request):
    return HttpResponse("Bienvenido a App 2 - Servicios")

def acerca_app2(request):
    return HttpResponse("App 2 - Acerca de Nosotros")