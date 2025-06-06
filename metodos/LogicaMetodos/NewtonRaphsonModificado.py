from sympy import symbols, sympify, lambdify, diff

def newtonRaphsonModificado(funcion, valorInicial, tolerancia, maxIteraciones = 100):
    x = symbols('x')

    try:
        funcion = funcion.replace('^', '**')
        funcionExp = sympify(funcion)

        derivada1 = diff(funcionExp, x)
        derivada2 = diff(derivada1, x)

        funcionEvaluable = lambdify(x, funcionExp, modules=['math'])
        funcionDerivada = lambdify(x, derivada1, modules=['math'])
        funcionSegundaDerivada = lambdify(x, derivada2, modules=['math'])

    except Exception as error:
        return {"error": "Error al convertir la función: " + str(error)}

    aproximacionActual = valorInicial
    historialIteraciones = []

    for iteracion in range(1, maxIteraciones +1):
        try:
            valorFuncion = funcionEvaluable(aproximacionActual)
            valorDerivada = funcionDerivada(aproximacionActual)
            valorSegundaDerivada = funcionSegundaDerivada(aproximacionActual)

            denominador = valorDerivada**2 - valorFuncion * valorSegundaDerivada

            if denominador == 0:
                return {"error": "Denominador cero en la iteración " + str(iteracion)}

            nuevaAproximacion = aproximacionActual - (valorFuncion * valorDerivada) / denominador
            error_aproximado = abs(nuevaAproximacion - aproximacionActual)

            historialIteraciones.append({
                "iteracion": iteracion,
                "aproximacion": aproximacionActual,
                "valorFuncion": valorFuncion,
                "valorDerivada": valorDerivada,
                "valorSegundaDerivada": valorSegundaDerivada,
                "nuevaAproximacion": nuevaAproximacion,
                "error_aproximado": error_aproximado
            })

            if error_aproximado < tolerancia:
                return {
                    "resultado": nuevaAproximacion,
                    "historial": historialIteraciones,
                    "convergencia": True
                }

            aproximacionActual = nuevaAproximacion

        except Exception as error:
            return {"error": "Error en la iteración " + str(iteracion) + ": " + str(error)}

    return {
        "resultado": aproximacionActual,
        "iteraciones": historialIteraciones,
        "convergencia": False,
        "error": "No se alcanzó la convergencia en el número máximo de iteraciones."
    }
