import imp
from pyexpat import model
from django.db import models
from django.utils.timezone import now

#CKEDITOR
from ckeditor.fields import RichTextField
# Create your models here.

class Services(models.Model):
    image = models.ImageField(verbose_name='Imagen', upload_to='service') 
    title = models.CharField(max_length=200, verbose_name='Título')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(default=now, verbose_name='Fecha de publicación')
    
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    
    class Meta:
        verbose_name= 'Service'
        verbose_name_plural= 'Services'
        ordering = ['created']
    
    def __str__(self):
        return f"title: {self.title} subtitle: {self.content}"
    
    