#Queremos que una funcion cuente la cantidad de letras
#que tiene un nombre y lo multiplique por un numero

def contar_letras(nombre,factor):
    nro = len(nombre)*factor
    print(nro)

contar_letras('Pablo',5)