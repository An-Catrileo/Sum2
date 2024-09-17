from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import ProductoForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    return redirect('Bienvenido a la aplicacion Juegos')


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

def vista_protegida(request):
    return render(request, 'juegos/protegida.html')

@login_required
def vista_protegida(request):
    return render(request, 'juegos/protegida.html')
#listar
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'juegos/listar.html', {'productos': productos})
#crear
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form= ProductoForm()
        return render (request, 'juegos/crear.html', {'form': form})
#editar
def editar_producto(request, pk):
    producto=get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
        else:
            form = ProductoForm(instance=producto)
        return render (request, 'juegos/editar.html', {'form':form})
#eliminar
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'juegos/eliminar.html', {'producto': producto})
        #@login required

def minecraft(request):
    return render(request, 'juegos/minecraft.html')

def mundo_abierto(request):
    return render(request, 'juegos/mundo_abierto.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso.')
            return redirect('index')
        else:
            messages.error(request, 'Por favor, corrija los errores a continuación.')
    else:
        form = UserCreationForm()
    return render(request, 'juegos/registro.html', {'form': form})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form =  ProductoForm(instance=producto)
        return render(request, 'juegos/editar.html', {'form': form})
    
    def eliminar_producto(request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        if request.method == 'POST':
            producto.delete()
            return redirect('listar_productos')
        return render(request, 'juegos/eliminar.html', {'producto': producto})
    


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
