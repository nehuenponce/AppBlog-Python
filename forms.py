from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class BlogsForm (forms.Form):
    titulo = forms.CharField(label="titulo" )
    subtitulo = forms.CharField(label="subtitulo" )
    parrafo = forms.CharField(label="parrafo")
    parrafoamplio = forms.CharField(label="parrafoamplio")
    autor = forms.CharField(label="autor" )
    creado= forms.DateField(label="creado")





class RegisterUsuarioForm(UserCreationForm):

    email= forms.EmailField(label="Email")
    password1= forms.CharField(label="password1", widget=forms.PasswordInput)
    password2= forms.CharField(label="password2", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}




class EditarUsuarioForm(UserCreationForm):

    email= forms.EmailField(label="Email")
    password1= forms.CharField(label="password1", widget=forms.PasswordInput)
    password2= forms.CharField(label="password2", widget=forms.PasswordInput)
    first_name= forms.CharField(label="Modificar Nombre")
    last_name= forms.CharField(label="Modificar Apellido")

    class Meta:
        model=User
        fields=["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}



class MensajeForm(forms.Form):
    emisor = forms.ModelChoiceField(queryset=User.objects.filter() ,label="emisor")
    receptor = forms.ModelChoiceField(queryset=User.objects.all() ,label="receptor")
    cuerpo = forms.CharField(label="cuerpo")