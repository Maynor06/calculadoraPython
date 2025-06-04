from sympy import symbols, sympify, lambdify, diff

def newton_raphson(funcion, valor_inicial, tolerancia, max_iteraciones=100):
    x = symbols('x')
    try:
        funcion = funcion.replace('^', '**')  # Corrige potencias si el usuario usa ^
        f_expr = sympify(funcion)
        f_derivada_expr = diff(f_expr, x)

        f = lambdify(x, f_expr, modules=['math'])
        f_derivada = lambdify(x, f_derivada_expr, modules=['math'])

    except Exception as error:
        return {"error": "Error al interpretar la función: " + str(error)}

    iteraciones = []
    xn = valor_inicial

    for i in range(1, max_iteraciones + 1):
        try:
            fxn = f(xn)
            fpxn = f_derivada(xn)

            if fpxn == 0:
                return {"error": "La derivada se anuló. Método no aplicable."}

            siguiente = xn - fxn / fpxn
            error_aprox = abs(siguiente - xn)

            iteraciones.append({
                "iteracion": i,
                "xn": xn,
                "f(xn)": fxn,
                "f'(xn)": fpxn,
                "xn+1": siguiente,
                "error": error_aprox
            })

            if error_aprox < tolerancia:
                return {
                    "resultado": siguiente,
                    "iteraciones": iteraciones,
                    "convergencia": True
                }

            xn = siguiente

        except Exception as e:
            return {"error": "Error durante la iteración: " + str(e)}

    return {
        "resultado": xn,
        "iteraciones": iteraciones,
        "convergencia": False,
        "error": "No se alcanzó la convergencia en el número máximo de iteraciones."
    }
