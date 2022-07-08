from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from tienda.models import  Mascota, Categoria
from .forms import ProductoForm, UserRegisterForm
from rest_framework import viewsets
from .serializers import  MascotaSerializer, CategoriaSerializer

 
class MascotaViewset(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class CategoriaViewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer




def index(request):
    return render(request, 'index.html')

def carrito_compra(request):
    return render(request, 'carrito_compra.html')

def gato(request):
    return render(request, 'gato.html')

def perro(request):
    return render(request, 'perro.html')


def quienesomos(request):
    return render(request, 'quienesomos.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return redirect('login')
    
    else:
        form = UserRegisterForm()
    context= {'form' : form}
    
    return render(request, 'register.html', context)


def formularioed(request, id):                                
            
    producto= get_object_or_404(Mascota, idProductomascota=id)
    contexto = {
        'form': ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='productos')
        contexto["form"]=formulario
            
    
    return render(request, 'formularioed.html', contexto)


def formularioel(request, id):
    
    mascota = get_object_or_404(Mascota, idProductomascota=id)
    mascota.delete()
    return redirect(to="productos")
    

def formularioag(request):
    data={
        'form': ProductoForm()
    }
    

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="guardado correctamente en la base de datos"
            return redirect(to='productos')
        else:
            data["form"]=formulario
    return render(request, 'formularioag.html', data)


def productos(request):
    
    mascota = Mascota.objects.all()
    contexto = {'mascotas':mascota}
    return render(request, 'productos.html', contexto)
