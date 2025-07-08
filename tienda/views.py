from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})


def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        imagen = request.POST.get('imagen')
        precio = request.POST.get('precio')

        if nombre and descripcion and imagen:
            Producto.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                imagen=imagen,
                precio=precio or 0
            )
            return redirect('inicio')  # o a donde desees redirigir
        else:
            error = "Por favor, llena todos los campos requeridos."
            return render(request, 'agregar_producto.html', {'error': error})
    productos = Producto.objects.all()
    return render(request, 'agregar_producto.html', {'productos': productos})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('agregar_producto')


def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.imagen = request.POST.get('imagen')
        producto.precio = request.POST.get('precio') or 0
        producto.save()
        return redirect('agregar_producto')

    return render(request, 'agregar_producto.html', {'producto': producto})
