from django.http import HttpResponse
from django.shortcuts import render
from metodos.LogicaMetodos.biseccion import biseccion
from metodos.forms import BiseccionForm


# Create your views here.

def inicio(request):
    return HttpResponse("Bienvenido a  la calculadora de métodos numéricos")

def viewBiseccion(request):
    resultado = None
    if request.method == "POST":
        form = BiseccionForm(request.POST)
        if form.is_valid():
            funcion = form.cleaned_data['funcion']
            puntoA = form.cleaned_data['puntoA']
            puntoB = form.cleaned_data['puntoB']
            tolerancia = form.cleaned_data['tolerancia']
            resultado = biseccion(funcion, puntoA, puntoB, tolerancia)
    else:
        form = BiseccionForm()

    return render(request, 'biseccion_formulario.html', {
        'form': form,
        'resultado': resultado
    })
