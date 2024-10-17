from django.urls import path
from .views import home, bootstrap_home
from .views import registrar_cita, registrar_medico, registrar_paciente, buscar_medicos
from . import views
from .views import buscar_medicos, listar_medicos
from django.contrib import admin


urlpatterns = [
    path('', home, name='home'), 
    path('bootstrap-home/', bootstrap_home, name='bootstrap_home'),  # Página con el template de Bootstrap
    path('registrar_medico/', registrar_medico, name='registrar_medico'),
    path('registrar_paciente/', views.registrar_paciente, name='registrar_paciente'),
    #path('buscar_medico', buscar_medicos, name='home'),
    #path('buscar_medico/', buscar_medicos, name='buscar_medico'),
    #path('buscar_medico/', views.buscar_medicos, name='buscar_medicos'),
    path('buscar_medico/', buscar_medicos, name='buscar_medicos'),
    path('medicos/', listar_medicos, name='listar_medicos')
]
