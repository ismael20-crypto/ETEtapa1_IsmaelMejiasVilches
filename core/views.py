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
           return redirect('pagina_principal')
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
    

'''Seralizers'''
from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import usuarios



@csrf_exempt
@api_view(['GET','POST'])

def lista_personas(request): 

    if request.method== 'GET':
        personas = creacion_usuario.objects.all()
        serializer =usuarios(personas, many=True)
        return Response(serializer.data)



    elif request.method=='POST': 
        data = JSONParser().parse(request)
        serializer = usuarios(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










