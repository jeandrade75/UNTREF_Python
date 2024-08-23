#Ver si un nuemro es par

def es_par():
    nro = int(input("Ingrese un número: "))
    if nro % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")

es_par()