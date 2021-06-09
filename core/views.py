from django.shortcuts import render

# Create your views here.

def pagina_p(request):

    return render (request , 'pagina_principal.html')

def galeria(request):

    return render (request , 'galeria.html')

def quienes_s(request):

    return render (request , 'quienes_somos.html')

