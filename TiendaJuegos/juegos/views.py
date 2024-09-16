from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


# Create your views here.


def index(request):
    return render(request, 'juegos/index.html')

def accion(request):
    return render(request, 'juegos/accion.html')

def gary_mod(request):
    return render(request, 'juegos/gary_mod.html')

def gta(request):
    return render(request, 'juegos/gta.html')

def kirby(request):
    return render(request, 'juegos/kirby.html')

def login(request):
    return render(request, 'juegos/login.html')

def minecraft(request):
    return render(request, 'juegos/minecraft.html')

def mundo_abierto(request):
    return render(request, 'juegos/mundo_abierto.html')

def registro(request):
    return render(request, 'juegos/registro.html')

def resident_evil(request):
    return render(request, 'juegos/resident_evil.html')

def subnautica(request):
    return render(request, 'juegos/subnautica.html')

def supermario(request):
    return render(request, 'juegos/supermario.html')

def supervivencia(request):
    return render(request, 'juegos/supervivencia.html')

def suspenso(request):
    return render(request, 'juegos/suspenso.html')

def terror(request):
    return render(request, 'juegos/terror.html')

def the_evil_within_2(request):
    return render(request, 'juegos/the_evil_within_2.html')

def the_witcher(request):
    return render(request, 'juegos/the_witcher.html')

def theforest(request):
    return render(request, 'juegos/theforest.html')

def todosLosJuegos(request):
    return render(request, 'juegos/todosLosJuegos.html')

def tom_raider(request):
    return render(request, 'juegos/tom_raider.html')

def zelda(request):
    return render(request, 'juegos/zelda.html')