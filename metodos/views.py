from django.http import HttpResponse
from django.shortcuts import render
from .LogicaMetodos import metodo_biseccion
# Create your views here.

def inicio(request):
    return HttpResponse("Bienvenido a  la calculadora de métodos numéricos")

def viewBiseccion(request):
    if request.method == "POST":
        funcion = request.POST.get("funcion")
        puntoA = float(request.POST.get("puntoA"))
        puntoB = float(request.POST.get("puntoB"))
        tolerancia = float(request.POST.get("tolerancia"))

        resultado = metodo_biseccion(funcion, puntoA, puntoB, tolerancia)

        return render(request, 'biseccion_resultado.html', {
            "funcion": funcion,
            "punto a": puntoA,
            "punto b": puntoB,
            "tolerancia": tolerancia,
            "resultado": resultado
        })

    return render(request, 'biseccion_form.html')
