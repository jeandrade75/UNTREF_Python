#Queremos que una funcion cuente la cantidad de letras
#que tiene un nombre y lo multiplique por un numero
#de no pasar ningun factor, entonces se multiplicara por 2

def contar_letras(nombre,factor=2):
    nro = len(nombre)*factor
    print(nro)

contar_letras('Pablo',5)
contar_letras('Pablo')