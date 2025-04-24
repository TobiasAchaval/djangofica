from django.shortcuts import render
from .models import Producto, Categoria

def tienda(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'tienda/tienda.html', {'productos': productos, 'categorias': categorias})
