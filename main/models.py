from django.db import models

class Main(models.Model):
    nome   = models.CharField(max_length=255, blank=False) 
    numero = models.CharField(max_length=255, blank=False)
    link   = models.CharField(max_length=255,blank=False)
    imagem = models.ImageField(upload_to="fotos/", blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#victor002
#Thenbhd2@
    def __str__(self):
        return self.numero

