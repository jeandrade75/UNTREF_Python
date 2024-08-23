#Crearemos una función donde deberemos mandar 
#nuestro nombre, apellido y edad por parámetros, 
#para poder después leerlo por terminal. 

#Luego modiﬁcaremos el código para solicitar los 
#mismos datos por terminar y mandarlos por parámetros.

def datos_personales(nombre,apellido,edad=0):
    Mis_datos =(nombre)+(apellido)+(edad)
    print(Mis_datos)

datos_personales('Pablo ','Andrade ',' 49 años')
