from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_app1, name='inicio1'),
    path('contacto/', views.contacto_app1, name='contacto1'),
]