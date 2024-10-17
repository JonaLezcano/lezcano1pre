from django.contrib import admin
from .models import Medico, Paciente, Cita, Especialidad

# Registra tus modelos en el admin de Django
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Cita)
admin.site.register(Especialidad)
