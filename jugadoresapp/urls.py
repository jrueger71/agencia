from django.urls import path
from . import views

urlpatterns = [
    path('', views.jugador_list, name='jugador_list'),
    path('jugador/<int:pk>/', views.jugador_detail, name='jugador_detail'),
    path('jugador/nuevo/', views.jugador_nuevo, name='jugador_nuevo'),
]
