from django import forms
from django.forms import ModelForm,widgets
from .models import creacion_u

class formulario_c(ModelForm):

    class meta :
        model =  creacion_u

        fields = ['nombre_f','apellido_f','edad_f','numero_t_f','fecha_nacimiento_f','genero_f','email_f','nombre_usuario_f','contrasena','contrasena2']

        labels={
            'nombre_f': 'Nombre',
            'apellido_f': 'Apellido',
            'edad_f': 'Edad',
            'numero_t_f': 'Numero de telefono',
            'fecha_nacimiento_f': 'Fecha de nacimiento',
            'genero_f': 'Genero',
            'email_f': 'Email ',
            'nombre_usuario_f': 'Nombre de usuario',
            'contrasena': 'Contraseña',
            
        }

        widgets ={
            'nombre_f': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ingrese su nombre',

                    'onchange': 'mayusculas()',
                    'onfocus': 'cambiarc(this)',
                    'onmouseout': 'volver(this)',
                    'minlength': '3',
                    'name':'nom'
                }
            ),

            'apellido_f': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'name': 'apellido',
                    'placeholder': 'ingrese su apellido',
                    'onchange': 'mayusculas2()',
                    'onfocus': 'cambiarc(this)',
                    'onmouseout': 'volver(this)',
                    'minlength': '5'
                }
            ),
            'edad_f': forms.TextInput(
                attrs={
                    'name': 'edad',
                    'class': 'form-control',
                    'placeholder': 'edad',
                    'min': '7',
                    'max': '100',
                    'maxlenght': '3'
                }
            ),

            'numero_t_f': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'name': 'numeroT',
                    'placeholder': '123456789',
                    'minlength': '9' ,
                    'onfocus': 'cambiarc(this)',
                    'onmouseout': 'volver(this)'
                }
            ),

            'fecha_nacimiento_f': forms.DateInput(
                attrs={
                    'name': 'fechaN',
                    'class': 'form-grop' ,
                    'min': '1921-01-01' 
                
                }
            ),

            'genero_f': forms.Select(
                attrs={
                    'class': 'form-control',
                    'name': 'genero'
                }

            ),
            'email_f': forms.TextInput(
                attrs={
                'class': 'form-control',
                'placeholder': 'fulanito@gmail.com',
                'name': 'email',
                'onfocus': 'cambiarc(this)',
                'onmouseout': 'volver(this)'
                }
            ),
            'nombre_usuario_f': forms.TextInput(
                attrs={
                    'name': 'NombreU',
                    'class': 'form-control',
                    'placeholder': 'ingrese su nombre de usuario',
                    'minlength': '8',
                    'onfocus': 'cambiarc(this)',
                    'onmouseout': 'volver(this)'

                }
            ),
            'contrasena' : forms.PasswordInput(
                attrs={
                    'class': 'from-control',
                    'name': 'contraseña' ,
                    'placeholder': 'ingrese su contraseña',
                    'minlength': '8' ,
                    'onfocus': 'cambiarc(this)',
                    'onmouseout': 'volver(this)'
                }
            )
    }


        