from django.urls import path 
from .views import pagina_p,galeria,quienes_s

urlpatterns = [
    path('',pagina_p, name="pagina_principal"),
    path('galeria', galeria, name="galeria"),
    path('quienes_s',quienes_s , name="quienes_somos")
]