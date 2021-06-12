from django.db import models

# Create your models here.

class genero(models.Model):
    id_genero = models.IntegerField(primary_key=True, verbose_name='id genero')
    genero = models.CharField(max_length=10,verbose_name='genero')


    def __str__(self):
        return(self.genero)

class creacion_u(models.Model):
    nombre_f = models.CharField(max_length=20 , verbose_name='Nombre')

    apellido_f = models.CharField(max_length=20,verbose_name='Apellido')

    edad_f = models.IntegerField(verbose_name='Edad')

    numero_t_f = models.IntegerField(verbose_name='Numero de celular')

    fecha_nacimiento_f = models.DateField(verbose_name='Fecha de nacimiento')

    genero_f = models.ForeignKey(genero ,on_delete=models.CASCADE)

    email_f = models.CharField(max_length=40, verbose_name='Email')

    nombre_usuario_f = models.CharField(primary_key=True, verbose_name='Nombre usuario', max_length=40)

    contrasena = models.CharField(max_length=40,verbose_name='contraseña')

    

    def __str__(self):
        return(self.nombre_usuario_f)