from django.db import models

# Clase que representa a los médicos en la cobertura médica
class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100, default="No especificada", null=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"

# Clase que representa a los pacientes
class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha = models.DateField()  
    
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
