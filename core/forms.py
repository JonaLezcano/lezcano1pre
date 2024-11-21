from django import forms
from .models import Paciente, Medico, Cita


class PacienteForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=128, label='Contraseña')

    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'email', 'password']  # Asegúrate de incluir todos los campos requeridos

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:  # Puedes ajustar la longitud mínima según tus necesidades
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Paciente.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nombre', 'apellido', 'especialidad', 'email']


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['paciente', 'medico', 'fecha_hora', 'motivo']
        widgets = {
            'fecha_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo Electrónico')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    
class PacienteUpdateForm(forms.ModelForm):
    new_password = forms.CharField(required=False, widget=forms.PasswordInput)

    class Meta:
        model = Paciente
        fields = ['telefono', 'dni', 'avatar']