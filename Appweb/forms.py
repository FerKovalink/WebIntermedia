from django import forms

class destinoFormulario(forms.Form):
    lugar = forms.CharField()
    fecha_desde = forms.DateField()
    fecha_hasta = forms.DateField()
    cantidad_de_personas = forms.IntegerField()

class pasajeroFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    edad = forms.IntegerField()

class alojamientoFormulario(forms.Form):
    nombre = forms.CharField()
    direccion = forms.CharField()
