from django.db import models

# Create your models here.

class ContactsDatabase(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    email = models.EmailField(verbose_name="E-mail")
    phone = models.IntegerField(verbose_name="Número de teléfono")
    msj = models.TextField(verbose_name="Mensaje")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Contacto")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última Modificación")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "contacto"
        verbose_name_plural = "contactos"
        ordering = ["-created"]