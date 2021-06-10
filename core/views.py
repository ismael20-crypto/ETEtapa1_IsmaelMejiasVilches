from django.shortcuts import render,redirect 
from .models import creacion_u
from .forms import formulario_c

# Create your views here.

def pagina_p(request):

    return render (request , 'pagina_principal.html')

def galeria(request):

    return render (request , 'galeria.html')

def quienes_s(request):

    return render (request , 'quienes_somos.html')

def form_creacion(request):

    if request.method=="POST":
        formulario_c=creacion_u(request.POST)
        if formulario_c.is_valid():
           formulario_c.save()
           return redirect('pagina_principal')
    else:
        formulario_c=creacion_u(request.POST)
    
    return render(request, 'core(2)/creacion_de_usuario', {'formulario_c': formulario_c})











