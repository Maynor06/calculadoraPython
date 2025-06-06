from django import forms


class BiseccionForm(forms.Form):
    funcion = forms.CharField (label="Función", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ej: x**3 - x - 2'}))
    puntoA = forms.FloatField(label='Punto A', required=True)
    puntoB = forms.FloatField(label='Punto B', required=True)
    tolerancia = forms.FloatField(label='Tolerancia', required=True)

class NewtonForm(forms.Form):
    funcion = forms.CharField(label="Función", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ej: x**2 - x - 2'}) )
    valorInicial = forms.FloatField(label='Valor Inicial', required=True)
    tolerancia = forms.FloatField(label='Tolerancia', required=True)

class NewtonRaphsonModificadoForm(forms.Form):
    funcion = forms.CharField(label="Función", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ej: x**3 - x - 2'}))
    valorInicial = forms.FloatField(label='Valor Inicial (x₀) ', required=True)
    tolerancia = forms.FloatField(label='Tolerancia', required=True)
    maxIteraciones = forms.IntegerField(label='Máximo de Iteraciones', initial=100, required=False)