from django import forms
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from me.models import canales


class canales(forms.Form):
    nombre = models.CharField(label='Nombre del Canal')
    url = models.CharField(label='URL')
    descripcion = models.CharField(label='Descripcion del canal')