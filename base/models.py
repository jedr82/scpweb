from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class ClaseModelo(models.Model):
    estado = models.BooleanField('Estado', default=True)
    fc = models.DateTimeField('Fecha de creación', auto_now_add=True)
    fm = models.DateTimeField('Ultima modificación', auto_now=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntegerField('Usuario de modificación', blank=True, null=True)

    class Meta:
        abstract = True