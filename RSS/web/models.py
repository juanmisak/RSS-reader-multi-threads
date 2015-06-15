from django.db import models

class canales(models.Model):
    nombre = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    pub_fecha = models.CharField(max_length=200)
    class Meta:
        verbose_name = "Canal"
        verbose_name_plural = "Canales"