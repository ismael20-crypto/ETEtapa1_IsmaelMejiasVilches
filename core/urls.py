from django.urls import path 
from .views import lista_personas, pagina_p,galeria,quienes_s,form_creacion,mostrar_u,modificar,eliminar,lista_personas

urlpatterns = [
    path('',pagina_p, name="pagina_principal"),
    path('galeria', galeria, name="galeria"),
    path('quienes_s',quienes_s , name="quienes_somos"),
    path('creacion_usuario',form_creacion, name="creacion_de_usuario"),
    path('Mostrar_usuario',mostrar_u, name="mostrar_u"),
    path('modificar/<id>',modificar,name="modificar"),
    path('elimina/<id>',eliminar,name="eliminar"),
    path('lista_personas', lista_personas, name="lista_personas")
]