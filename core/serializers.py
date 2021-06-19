from rest_framework import serializers

from .models import creacion_usuario 

class usuarios(serializers.ModelSerializer):

    class Meta: 

        model = creacion_usuario

        fields = ['nombre_f', 'apellido_f', 'edad_f', 'numero_t_f','fecha_nacimiento_f','genero_f','email_f','nombre_usuario_f','contrasena']
