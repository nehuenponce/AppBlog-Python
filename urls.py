from os import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('../AppBlog/index.html',inicio, name="inicio"),
    path('usuario/registro.html',register, name="register"),
    path('usuario/login.html', login_register, name="login"),
    path('usuario/logout.html', LogoutView.as_view(), name="logout"),


    path('Blog/crearblog.html', crearblog, name="crearblog"),
    path('Mensajeria/crearmensaje.html', crearmensaje, name="crearmensaje"),


    path('about/about.html',about, name="about"),
    path('Pagina/pagina2.html',pagina2, name="pagina2"),

    
    path('Blog/blog.html <id>',blog, name="blog"),
    path('Blog/blog1.html',blog1, name="blog1"),
    path('Blog/blog2.html',blog2, name="blog2"),
    path('Blog/blog3.html',blog3, name="blog3"),
    path('Blog/blog4.html',blog4, name="blog4"),

    path('autortitlesearch/constrccion.html',construccion, name="construccion"),


    path('buscar/',buscar, name="buscar"),
    path('autortitlesearch/busquedatitulo.html', busquedatitulo, name="busquedatitulo"),

    
    path('Blog/eliminarblog.html/<id>',eliminarblog, name="eliminarblog"),
    path('Blog/editarblog.html/<id>',editarblog, name="editarblog"),
    path('usuario/editarperfil.html', editarperfil, name="editarperfil"),
   

    path('Blog/listadeblog.html', listadeblog, name="listadeblog"),
    path('Mensajeria/listademensaje.html', listademensaje, name="listademensaje"),

]