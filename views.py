from django.shortcuts import render
from django.http import HttpResponse

from ..AppBlog.forms import BlogsForm, RegisterUsuarioForm, EditarUsuarioForm, UserCreationForm , MensajeForm
from ..AppBlog.models import Blogs , Mensaje



from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 



def inicio(request):
    return render(request, "../AppBlog/index.html")

def about(request):
    return render(request, "about/about.html")

def pagina2(request):
    return render(request, "Pagina/pagina2.html")

def construccion(request):
    return render(request, "autortitlesearch/constrccion.html")



#Blogs inicios

def blog1(request):
    return render(request, "Blog/blog1.html")

def blog2(request):
    return render(request, "Blog/blog2.html")

def blog3(request):
    return render(request, "Blog/blog3.html")

def blog4(request):
    return render(request, "Blog/blog4.html")



#Todo sobre usuarios

def register(request):
    if request.method=="POST":
        form= RegisterUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "usuario/registro.html", {"mensaje": f"usuario {username} creado correctamente"} )
        else:
            return render(request, "usuario/registro.html", {"form": form, "mensaje":"Error al crear el usuario."})
    else:
        form= RegisterUsuarioForm()
        return render (request, "usuario/registro.html", {"form": form})
        
    
def login_register(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "../AppBlog/index.html", {"mensaje": f"{usu} logeado correctamente."})
            else:
                return render(request, "usuario/login.html", {"form":form, "mensaje":"usuario o contraseña incorrecta."})
        else:        
            return render(request, "usuario/login.html", {"form":form, "mensaje":"usuario o contraseña incorrecta."})
    else:
        form= AuthenticationForm()
        return render(request, "usuario/login.html", {"form": form})

@login_required
def editarperfil(request):
    usuario= request.user
    if request.method=="POST":
        form=EditarUsuarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "usuario/editarperfil.html" , { "mensaje": f"Usuario {usuario.username} editado correctamente."} )
        else:
            return render(request, "usuario/editarperfil.html" , {"form" : form , "nombreusuario":usuario.username})
    else:
        form=EditarUsuarioForm(instance=usuario)
        return render(request, "usuario/editarperfil.html" , {"form" : form , "nombreusuario":usuario.username} )


@login_required
#Todo sobre Blogs

def crearblog (request):
    if request.method=="POST":
        form= BlogsForm(request.POST, request.FILES)
        if form.is_valid():
            informacion= form.cleaned_data 
            titulo= informacion["titulo"]
            subtitulo= informacion["subtitulo"]
            parrafo= informacion["parrafo"]
            parrafoamplio= informacion["parrafoamplio"]
            autor= informacion["autor"]
            creado= informacion["creado"]
            imagen= informacion["imagen"]
            blo= Blogs(titulo=titulo, subtitulo=subtitulo, parrafo=parrafo, parrafoamplio=parrafoamplio, autor=autor, creado=creado)
            blo.save()
            return render(request, "Blog/crearblog.html", {"mensaje": "Blog guardado"})
        else:
            return render(request, "Blog/crearblog.html", {"mensaje2": "Informacion no Valida para guardar."})
    else:
        formulario= BlogsForm()
        return render(request, "Blog/crearblog.html", {"form": formulario})



def eliminarblog(request, id):
    ti= Blogs.objects.get(id=id)
    ti.delete()
    titu= Blogs.objects.all()
    return render(request, "autortitlesearch/resultadoautor.html", {"autor": titu, "mensaje": "Blog eliminado."})


def listadeblog (request):
    blogs= Blogs.objects.filter()
    return render(request, "Blog/listadeblog.html", {"blog" : blog})



def editarblog (request, id):
    edi=Blogs.objects.get(id=id)
    if request.method=="POST":
        form= BlogsForm(request.POST, request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            edi.titulo=info["titulo"]
            edi.subtitulo=info["subtitulo"]
            edi.parrafo=info["parrafo"]
            edi.parrafoamplio=info["parrafoamplio"]
            edi.autor=info["autor"]
            edi.creado=info["creado"]
            edi.save()
            blogs=Blogs.objects.all()
            return render(request, "Blog/listadeblog.html", { "blogs":blogs ,"mensaje":"Blog editado correctamente."})
    else:
        formulario= BlogsForm(initial={"titulo":edi.titulo, "subtitulo":edi.subtitulo, "parrafo":edi.parrafo, "parrafoamplio":edi.parrafoamplio, "autor":edi.autor ,"creado":edi.creado})
        return render(request, "usuario/editarperfil.html", {"form": formulario, "blogs": edi})


def busquedatitulo (request):
    return render(request, "autortitlesearch/busquedatitulo.html")


def buscar (request):
    titulo= request.GET["titulo"]
    if titulo!="":
        titu= Blogs.objects.filter(titulo__icontains=titulo)
        return render(request, "autortitlesearch/resultadoautor.html" ,{"titu":titu})
    else:
        return render(request, "autortitlesearch/busquedatitulo.html", {"mensaje":"Ingresa por favor un Titulo."})



def blog(request, id):
    blogs= Blogs.objects.filter(id=id)
    return render(request, "Blog/blog.html", {"blogs" : blogs})





# Chat de mensajeria 

def crearmensaje (request):
    if request.method=="POST":
        form= MensajeForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            emisor= informacion["emisor"]
            receptor= informacion["receptor"]
            cuerpo= informacion["cuerpo"]
            men= Mensaje(emisor=emisor, receptor=receptor, cuerpo=cuerpo)
            men.save()
            return render(request, "Mensajeria/crearmensaje.html", {"mensaje": "Mensaje enviado."})
        else:
            return render(request, "Mensajeria/crearmensaje.html", {"mensaje2": "Informacion no Valida para enviar."})
    else:
        formulario= MensajeForm()
        return render(request, "Mensajeria/crearmensaje.html", {"form": formulario})



def listademensaje(request):
    msj= Mensaje.objects.filter()
    return render(request, "Mensajeria/listademensaje.html", {"msj" : msj})