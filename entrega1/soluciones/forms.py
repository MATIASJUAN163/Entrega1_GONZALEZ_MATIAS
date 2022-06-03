from django import forms

class ModemFormulario(forms.Form):

    marca = forms.CharField( max_length=40 )
    modelo = forms.CharField( max_length=40 )
    comunicacion = forms.CharField( max_length=40 )
    precio = forms.FloatField()

class MeterFormulario(forms.Form):
    
    marca = forms.CharField( max_length=40 )
    modelo = forms.CharField( max_length=40 )
    tipo = forms.CharField( max_length=40 )
    precio = forms.FloatField()
    
class WebFormulario(forms.Form):
    
    marca = forms.CharField( max_length=40 )
    modelo = forms.CharField( max_length=40 )
    precio = forms.FloatField()
    