from django.shortcuts import render,redirect 
from .models import creacion_usuario
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
           return redirect('mostrar_u')
    else:
        formulario=formulario_c()
    
    return render(request, 'core(2)/creacion_de_usuario.html', {'formulario_c': formulario_c})

def mostrar_u(request):
    personas = creacion_usuario.objects.all()
    return render (request , 'core(2)/mostrar_personas.html', {'personas':personas})

def modificar(request,id):

    usuario = creacion_usuario.objects.get(nombre_usuario_f=id)

    datos ={
        'form' :formulario_c(instance=usuario)
    }
    if request.method == "POST":
        formulario2=formulario_c(data=request.POST,instance=usuario)
        if formulario2.is_valid():
           formulario2.save()
           return redirect('mostrar_u')
    else:
        formulario2=formulario_c()
    
    return render(request, 'core(2)/modificar_persona.html', datos)



def eliminar(request,id):

    persona_e =creacion_usuario.objects.get(nombre_usuario_f=id)
    persona_e.delete()
    return redirect('mostrar_u')
    








