from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password

class Medico(models.Model):
    ESPECIALIDADES = [
       ('clinico', 'Clínico'),
        ('pediatria', 'Pediatría'),
        ('traumatologia', 'Traumatología'),
        ('cardiologia', 'Cardiología'),
        ('dermatologia', 'Dermatología'),
    ] 
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=20, choices=ESPECIALIDADES)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Campo para contraseña encriptada

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"

class PacienteManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Asegúrate de incluir el username al crear el superusuario
        if 'username' not in extra_fields:
            extra_fields['username'] = email  # Usar el email como username

        return self.create_user(email, password, **extra_fields)

class Paciente(AbstractUser):
    username = models.CharField(max_length=150, unique=True, blank=False)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True)
    dni = models.CharField(max_length=20, blank=True)

    USERNAME_FIELD = 'email'  # Definimos el email como nombre de usuario
    REQUIRED_FIELDS = ['username']  # Asegúrate de que el campo username sea requerido

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Clase que representa las citas
class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    motivo = models.TextField()

    def __str__(self):
        return f"Cita de {self.paciente} con {self.medico} el {self.fecha_hora}"

# Clase que representa las especialidades médicas disponibles
class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
