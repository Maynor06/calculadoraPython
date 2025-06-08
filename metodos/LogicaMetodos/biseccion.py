from sympy import *

def biseccion(funcion, puntoA, puntoB, tolerancia, max_iteraciones = 100):
    x = symbols('x')
    try:
        funcion = funcion.replace('^', '**')
        funcionExp = sympify(funcion)
        funcionEvaluable = lambdify(x, funcionExp)
    except Exception as error:
        return {"error": "Error al convertir la función: " + (error)}

    puntoAcalculada = funcionEvaluable(puntoA)
    puntoBcalculada = funcionEvaluable(puntoB)

    if puntoAcalculada * puntoBcalculada > 0:
        return {"error": "Los puntos A y B no encierran una raíz."}

    iteraciones = []
    for i in range(1, max_iteraciones + 1):
        puntoMedio = (puntoA + puntoB) / 2
        puntoMedioCalculado = funcionEvaluable(puntoMedio)
        errorAbsoluto = abs(puntoB - puntoA) / 2

        iteraciones.append({
            "iteracion": i,
            "puntoA": puntoA,
            "puntoB": puntoB,
            "puntoMedio": puntoMedio,
            "puntoMedioCalculado": puntoMedioCalculado,
            "errorAbsoluto": errorAbsoluto
        })

        if abs(puntoMedio) < tolerancia or errorAbsoluto < tolerancia:
            return {
                "resultado": puntoMedio,
                "iteraciones": iteraciones,
                "convergencia": True
            }

        if puntoAcalculada * puntoMedioCalculado < 0:
            puntoB = puntoMedio
            puntoBcalculada = puntoMedioCalculado
        else:
            puntoA = puntoMedio
            puntoAcalculada = puntoMedioCalculado

    return {
        "resultado": puntoMedio,
        "iteraciones": iteraciones,
        "convergencia": False,
        "error": "No se alcanzó la convergencia en el número máximo de iteraciones."
    }