from django.urls import path
from .views import home, bootstrap_home, registrar_paciente, registrar_medico, listar_medicos, registrar_cita, buscar_medicos, about_me, login_view, perfil_view
from .views import CitasListView
from . import views

from django.contrib import admin


urlpatterns = [
    path('', home, name='home'),  # Página de inicio
    path('bootstrap-home/', bootstrap_home, name='bootstrap_home'),  # Página con el template de Bootstrap
    path('registrar_medico/', registrar_medico, name='registrar_medico'),  # Página para registrar médico
    path('registrar_paciente/', registrar_paciente, name='registrar_paciente'),  # Página para registrar paciente
    path('registrar_cita/', registrar_cita, name='registrar_cita'),  # Página para registrar cita
    path('medicos/', listar_medicos, name='listar_medicos'),  # Página para listar médicos
    path('about/', about_me, name='about_me'),  # Página de 'About Me
    path('login/', login_view, name='iniciar_sesion'),
    path('perfil/', perfil_view, name='perfil'),
    path('logout/', views.logout_view, name='logout'),
    path('buscar_medicos/', buscar_medicos, name='buscar_medicos'),
    path('mis_citas/', CitasListView.as_view(), name='mis_citas'),

]