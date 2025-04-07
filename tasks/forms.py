# forms.py
from django import forms
from .models import SolicitudServicio, Servicio

class SolicitudServicioForm(forms.ModelForm):
    class Meta:
        model = SolicitudServicio
        fields = ['servicio', 'mensaje', 'nombre', 'direccion', 'telefono', 'email']

    servicio = forms.ModelChoiceField(queryset=Servicio.objects.all())  # Los servicios disponibles
