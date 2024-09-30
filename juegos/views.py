from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import ProductoForm
from django.http import HttpResponse

# Create your views here.
@login_required
def home(request):
    context = {
        'is_superuser': request.user.is_superuser,
    }
    return render(request, 'juegos/home.html', context)


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

def vista_protegida(request):
    return render(request, 'juegos/protegida.html')

@login_required
def vista_protegida(request):
    return render(request, 'juegos/protegida.html')
#listar
@login_required
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'juegos/listar.html', {'productos': productos})
#crear
@login_required
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
@login_required
def editar_producto(request, pk):
    producto=get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'juegos/editar.html', {'form':form})
    
    
#eliminar
@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'juegos/eliminar.html', {'producto': producto})


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
            return redirect("listar_productos")
    else:
        form = UserCreationForm()
    return render(request, 'juegos/registro.html', {'form': form})


    
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

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'juegos/login.html'

def get_success_url(self):
        #Si es superusuario, redirigir al panel de administración
    if self.request.user.is_superuser:
        return '/admin/' #puedes redirigir a cualquiera otra pagina especial para superusuario
        #Si es un usuario normal, redirigir a la lista de productos
    return redirect('listar_productos')
    
    
from django.contrib.auth.models import User


@login_required
def perfil_usuario(request):
    if request.user.is_superuser:
        usuarios = User.objects.all()
    else:
        usuarios = None

    context = {
        'user': request.user,
        'usuarios':usuarios,
    }

    return render(request, 'juegos/perfil.html', context)



def agregar_al_carrito(request, producto_id):
    # Obtener el producto o devolver un error 404 si no existe
    producto = get_object_or_404(Producto, id=producto_id)
    
    # Obtener el carrito de la sesión, si no existe, inicializarlo como un diccionario vacío
    carrito = request.session.get('carrito', {})
    
    # Si el producto ya está en el carrito, incrementar la cantidad
    if producto_id in carrito:
        carrito[producto_id]['cantidad'] += 1
    else:
        # Agregar el producto al carrito con la cantidad inicial de 1
        carrito[producto_id] = {
            'nombre': producto.nombre,
            'precio': float(producto.precio),  # Convertimos a float para evitar problemas de JSON
            'cantidad': 1,
        }
    
    # Guardar el carrito en la sesión
    request.session['carrito'] = carrito
    
    # Redirigir a la lista de productos o a la vista del carrito
    return redirect('listar_productos')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    total = 0
    for producto_id, item in carrito.items():
        item['total'] = item['precio'] * item['cantidad']
        total += item['total']
        
    return render(request, 'juegos/ver_carrito.html', {'carrito': carrito, 'total': total})


def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    
    # Si el producto está en el carrito, eliminarlo
    if producto_id in carrito:
        del carrito[producto_id]
    
    # Actualizar el carrito en la sesión
    request.session['carrito'] = carrito
    
    return redirect('ver_carrito')

def vaciar_carrito(request):
    # Vaciar el carrito en la sesión
    request.session['carrito'] = {}
    
    return redirect('ver_carrito')

from django.shortcuts import redirect

def actualizar_cantidad_carrito(request, producto_id):
    if request.method == 'POST':
        nueva_cantidad = int(request.POST.get('cantidad', 1))
        carrito = request.session.get('carrito', {})
        
        producto_id_str = str(producto_id)
        
        if producto_id_str in carrito:
            if nueva_cantidad > 0:
                carrito[producto_id_str]['cantidad'] = nueva_cantidad
            else:
                del carrito[producto_id_str]  # Eliminar el producto si la cantidad es 0
        
        request.session['carrito'] = carrito
        
    return redirect('ver_carrito')


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated]) #Requiere autenticación
def productos_api(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


import requests
from django.shortcuts import render

def listar_categorias_juegos(request):
    url = "https://rawg.io/"  # URL de la API
    response = requests.get(url)  # Realizar la solicitud GET a la API
    data = response.json()  # Convertir la respuesta a formato JSON
    categorias = data['categories']  # Obtener las categorías de juegos
    return render(request, 'juegos/listar_categorias_juegos.html', {"categorias": categorias})

