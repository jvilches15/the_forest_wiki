from django.shortcuts import render, redirect
from .forms import RegistroFormulario  
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)  
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('menu')  
    else:
        form = RegistroFormulario()  
    return render(request, 'registrase_wiki.html', {'form': form})



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('menu')  
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
        else:
            messages.error(request, "Datos inválidos, intenta nuevamente")
    else:
        form = AuthenticationForm()
    
    return render(request, 'inicio_sesion_wiki.html', {'form': form})

def home(request):
    return redirect(reverse('login'))

def menu_view(request):
    return render(request, 'menuprincipal_wiki.html')



def animales_view(request):
    return render (request, 'Animales.html')

def armas_view(request):
    return render (request, 'Armas.html')

def construcciones_view(request):
    return render (request, 'Construcciones.html')

def consumibles_view(request):
    return render (request, 'Consumibles.html')

def enemigos_view(request):
    return render (request, 'Enemigos.html')

def flora_view(request):
    return render (request, 'Flora.html')

def forowiki_view(request):
    return render (request, 'forowiki.html')

def historia_view(request):
    return render (request, 'historia.html')

def logros_view(request):
    return render (request, 'Logros.html')

def lugarestf_view(request):
    return render (request, 'Lugarestf.html')

def micuentatf_view(request):
    return render (request, 'micuentatf.html')

def recuperacontra_view(request):
    return render (request, 'recuperarcontra.html')






# Create your views here.
