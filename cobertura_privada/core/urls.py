from django.urls import path
from .views import home, bootstrap_home
from .views import registrar_cita, registrar_medico, registrar_paciente, buscar_medicos
from . import views
from .views import buscar_medicos, listar_medicos, about_me
from django.contrib import admin


urlpatterns = [
    path('', home, name='home'),  # Página de inicio
    path('bootstrap-home/', bootstrap_home, name='bootstrap_home'),  # Página con el template de Bootstrap
    path('registrar_medico/', registrar_medico, name='registrar_medico'),  # Página para registrar médico
    path('registrar_paciente/', registrar_paciente, name='registrar_paciente'),  # Página para registrar paciente
    path('registrar_cita/', registrar_cita, name='registrar_cita'),  # Página para registrar cita
    path('buscar_medico/', buscar_medicos, name='buscar_medicos'),  # Página para buscar médicos
    path('medicos/', listar_medicos, name='listar_medicos'),  # Página para listar médicos
    path('about/', about_me, name='about_me'),  # Página de 'About Me
]
