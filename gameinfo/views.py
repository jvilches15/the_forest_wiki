from django.shortcuts import render


def home(request):
    return render(request, 'inicio_sesion_wiki.html')

def login_view(request):
    return render(request, 'inicio_sesion_wiki.html')

def menu_view(request):
    return render(request, 'menuprincipal_wiki.html')

def registrarse_view(request):
    return render(request, 'registrase_wiki.html')

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

def registrase_wiki_view(request):
    return render (request, 'registrase_wiki.html')

# Create your views here.
