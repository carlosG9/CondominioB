from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('administrador/', views.administrador, name='admin'),
    path('residente/', views.residente, name='residente'),
]
