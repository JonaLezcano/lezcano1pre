from django.shortcuts import render, redirect   
from .forms import PacienteForm, MedicoForm, CitaForm
from .models import Medico, Paciente
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db.models import Q




def home(request):
    return render(request, 'home.html', {'user': request.user})

def bootstrap_home(request):
    return render(request, 'bootstrap_home.html')

def registrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            # Crear una instancia de Paciente a partir del formulario
            paciente = form.save(commit=False)

            # Generar el username a partir del email
            email = form.cleaned_data['email']
            username = email.split('@')[0]  # Usar la parte del email antes del @

            # Verificar si el nombre de usuario ya existe y ajustar si es necesario
            while Paciente.objects.filter(username=username).exists():
                username += str(Paciente.objects.filter(username=username).count())

            paciente.username = username  # Asignar el username generado
            paciente.set_password(form.cleaned_data['password'])  # Asegúrate de establecer la contraseña correctamente
            paciente.save()

            messages.success(request, 'Paciente registrado exitosamente.')
            return redirect('home')  
    else:
        form = PacienteForm()
    
    return render(request, 'registrar_paciente.html', {'form': form})

def registrar_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('listar_medicos') 
    else:
        form = MedicoForm()
    return render(request, 'registrar_medico.html', {'form': form})



def listar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'listar_medicos.html', {'medicos' : medicos})

def registrar_cita(request):
    if request.method == 'POST':
        
        medico = request.POST.get('medico')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        
           
        return redirect('home')
    else:
        
        medicos = Medico.objects.all() 
        return render(request, 'registrar_cita.html', {'medicos': medicos})
    
def buscar_medicos(request):
    query = request.GET.get('q')  # Obtiene el término de búsqueda de la URL
    resultados = Medico.objects.all()  # Por defecto, obtiene todos los médicos

    if query:  # Si hay un término de búsqueda
        # Filtra por nombre, apellido o especialidad (asumiendo que tienes esos campos en tu modelo)
        resultados = resultados.filter(
            Q(nombre__icontains=query) |  # Busca en el campo 'nombre'
            Q(apellido__icontains=query) |  # Busca en el campo 'apellido'
            Q(especialidad__icontains=query)  # Busca en el campo 'especialidad'
        )

    return render(request, 'buscar_medico.html', {'resultados': resultados})

def about_me(request):
    return render(request, 'about_me.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('perfil')  # Redirige a la vista del perfil
            else:
                form.add_error(None, 'Credenciales inválidas')  # Mensaje de error si las credenciales son incorrectas
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def perfil_view(request):
    user = request.user
    if request.method == 'POST':
        if 'avatar' in request.FILES:
            user.avatar = request.FILES['avatar']
        
        # Actualiza los campos adicionales
        user.telefono = request.POST.get('telefono', user.telefono)
        user.dni = request.POST.get('dni', user.dni)
        
        # Manejo de la nueva contraseña
        new_password = request.POST.get('new_password')
        if new_password:
            user.password = make_password(new_password)  # Encriptar nueva contraseña
        
        user.save()
        return redirect('perfil')  # Redirige de nuevo al perfil tras la actualización

    return render(request, 'perfil.html', {'user': user})

def logout_view(request):
    logout(request)
    return redirect('home')