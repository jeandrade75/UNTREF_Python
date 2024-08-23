#Conjetura de Collatz
#El while lo va a ejecutar mientras la condicion sea True

#Al Ingresar un numero, si es para, debe dividirse por 2
#Si es impar, debe multiplicarse por tres y sumarse uno
#El resultado debe pasar por el mismo proceso. Eventualmente siempre terminara en 1

nro=int (input('Ingrese numero: '))

while nro != 1:
    if nro % 2 == 0:
        nro = int( nro / 2 )
    else:
        nro = int( nro * 3 + 1 )
print(nro)
