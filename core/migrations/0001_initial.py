# Generated by Django 3.2.4 on 2021-06-11 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='genero',
            fields=[
                ('id_genero', models.IntegerField(primary_key=True, serialize=False, verbose_name='id genero')),
                ('genero', models.CharField(max_length=10, verbose_name='genero')),
            ],
        ),
        migrations.CreateModel(
            name='creacion_u',
            fields=[
                ('nombre_f', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellido_f', models.CharField(max_length=20, verbose_name='Apellido')),
                ('edad_f', models.IntegerField(verbose_name='Edad')),
                ('numero_t_f', models.IntegerField(verbose_name='Numero de celular')),
                ('fecha_nacimiento_f', models.DateField(verbose_name='Fecha de nacimiento')),
                ('email_f', models.CharField(max_length=40, verbose_name='Email')),
                ('nombre_usuario_f', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Nombre usuario')),
                ('contrasena', models.CharField(max_length=40, verbose_name='contraseña')),
                ('genero_f', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.genero')),
            ],
        ),
    ]
