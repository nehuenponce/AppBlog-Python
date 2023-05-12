from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Blogs (models.Model):
    titulo = models.CharField (max_length=60)
    subtitulo = models.CharField (max_length=60)
    parrafo= models.CharField (max_length=100)
    parrafoamplio= models.CharField(max_length=900)
    autor= models.CharField (max_length=60)
    creado= models.DateField(auto_created=False, auto_now=False, blank=True)
    imagen= models.ImageField(upload_to="blogs")
 
    def __str__(self):
        return f"{(self.titulo)} - {(self.subtitulo)} - {(self.parrafo)} - {(self.autor)}"


class Mensaje (models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="emisor")
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receptor")
    cuerpo = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{(self.emisor)} - {(self.receptor)} {(self.cuerpo)}"