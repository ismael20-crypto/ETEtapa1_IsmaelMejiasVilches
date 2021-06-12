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

    if request.method == "POST":
        formulario=formulario_c(request.POST)
        if formulario.is_valid():
           formulario.save()
           return redirect('pagina_principal')
    else:
        formulario=formulario_c()
    
    return render(request, 'core(2)/creacion_de_usuario.html', {'formulario_c': formulario})











