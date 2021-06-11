from django.urls import path 
from .views import pagina_p,galeria,quienes_s,form_creacion

urlpatterns = [
    path('',pagina_p, name="pagina_principal"),
    path('galeria', galeria, name="galeria"),
    path('quienes_s',quienes_s , name="quienes_somos"),
    path('creacion_usuario',form_creacion, name="creacion_de_usuario")
]