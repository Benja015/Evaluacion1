from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_app2, name='inicio2'),
    path('acerca/', views.acerca_app2, name='acerca2'),
]