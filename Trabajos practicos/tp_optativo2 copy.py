""" Trabajo Práctico Optativo

Integrando el código:
Armen dos bloques de código distinto. En uno usen una
forma de función, un for y una estructura de decisión. En
el segundo, otra forma de función, un while y otra
estructura de decisión. Utilicen distintos comparadores. """

def contar_y_comparar():
    numero = 1
    while numero <= 10:
        if numero < 5:
            print(f"{numero} es menor que 5")
        else:
            print(f"{numero} es mayor o igual que 5")
        numero += 1

# Ejemplo de uso
contar_y_comparar()

