from django.shortcuts import render, redirect   
from .forms import PacienteForm, MedicoForm, CitaForm
from .models import Medico

def home(request):
    return render(request, 'home.html')

def bootstrap_home(request):
    return render(request, 'bootstrap_home.html')

def registrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
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
        return render(request, 'crear_cita.html', {'medicos': medicos})
    
def buscar_medicos(request):
    query = request.GET.get('q', '')
    medicos = Medico.objects.filter(nombre__icontains=query) | Medico.objects.filter(apellido__icontains=query)

    context = {
        'medicos': medicos,
        'query': query,
    }
    return render(request, 'buscar_medico.html', context)

def about_me(request):
    return render(request, 'about_me.html')