from django.http import HttpResponse
from django.shortcuts import render

from metodos.LogicaMetodos.NewthonRaphson import newton_raphson
from metodos.LogicaMetodos.NewtonRaphsonModificado import newtonRaphsonModificado
from metodos.LogicaMetodos.biseccion import biseccion
from metodos.forms import BiseccionForm, NewtonForm, NewtonRaphsonModificadoForm

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

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

def viewNewton(request):
    resultado = None
    if request.method == "POST":
        form = NewtonForm(request.POST)
        if form.is_valid():
            funcion = form.cleaned_data['funcion']
            valorInicial = form.cleaned_data['valorInicial']
            tolerancia = form.cleaned_data['tolerancia']
            resultado = newton_raphson(funcion, valorInicial, tolerancia)
    else:
        form = NewtonForm()
    print(resultado)
    return render(request, 'newton.html', {
        'form': form,
        'resultado': resultado
    })

def viewNewtonRaphsonModificado(request):
    resultado = None
    if request.method == "POST":
        form = NewtonRaphsonModificadoForm(request.POST)
        if form.is_valid():
            funcion = form.cleaned_data['funcion']
            valorInicial = form.cleaned_data['valorInicial']
            tolerancia = form.cleaned_data['tolerancia']

            resultado = newtonRaphsonModificado(funcion, valorInicial, tolerancia)
    else:
        form = NewtonRaphsonModificadoForm()

    return render(request, 'newtonRaphsonModificado.html', {
        'form': form,
        'resultado': resultado
    })