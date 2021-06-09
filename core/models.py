from django.db import models

# Create your models here.

class genero(models.model):
    id_genero= model.IntergerField(primaryKey=True, verbose_name='id genero')
    genero= model.CharField(max_lenght=10,verbose_name='genero')


    def __str__ (self):

        return(self.genero)

def creacion_u(models.model):
    nombre_f= model.CharField(min_lenght=3 , verbose_name='Nombre')

    apellido_f= model.CharField(min_lenght=5,verbose_name='Apellido')

    edad_f= model.IntergerField(verbose_name='Edad')

    numero_t_f= model.IntergerField(max_lenght=9,verbose_name='Numero de celular')

    fecha_nacimiento_f= model.DateField(verbose_name='Fecha de nacimiento')

    genero_f= models.ForeignKey( genero ,on_delete=models.CASCADE)

    email_f= model.CharField(min_lenght=2, verbose_name='Email')

    nombre_usuario_f= model.CharField(primary_key=True, verbose_name='Nombre usuario')

    contrasena= model.CharField(min_lenght='3',verbose_name='contrae')

    def __str__ (self)
        return(self.nombre_usuario_f)