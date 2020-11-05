from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('administrador/', views.administrador, name='admin'),
    path('administrador/editar/<str:id_visits>/',
         views.administrador_editar, name='admin_editar'),
    path('administrador/eliminar/<str:id_visits>/',
         views.administrador_eliminar, name='admin_eliminar'),
    path('residente/', views.residente, name='residente'),
]
