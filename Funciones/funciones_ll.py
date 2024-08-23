#Ver si un nuemro es par


def es_par(nro):
    #nro = int(input("Ingrese un número: "))
    if nro % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")

es_par(10)
es_par(1002546)
es_par(11255550)
es_par(100022555)