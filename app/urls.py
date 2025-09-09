from django.urls import path
from . import views

urlpatterns = [
    path('dispositivos/', views.listar_dispositivos, name='listar_dispositivos'),
]
