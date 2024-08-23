""" Trabajo Práctico Optativo

Integrando el código:
Armen dos bloques de código distinto. En uno usen una
forma de función, un for y una estructura de decisión. En
el segundo, otra forma de función, un while y otra
estructura de decisión. Utilicen distintos comparadores. """

def procesar_numeros(numeros):
    resultados = []
    for numero in numeros:
        if numero % 2 == 0:
            resultados.append(f"{numero} es par")
        elif numero % 2 != 0:
            resultados.append(f"{numero} es impar")
        else:
            resultados.append(f"No se pudo determinar la paridad de {numero}")
    return resultados

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
resultado = procesar_numeros(numeros)
for r in resultado:
    print(r)
