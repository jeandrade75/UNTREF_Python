def solicitar_datos():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))
    return nombre, apellido, edad

def procesar_datos(nombre, apellido, edad):
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Edad: {edad}")

# Llamada a las funciones
nombre, apellido, edad = solicitar_datos()
procesar_datos(nombre, apellido, edad)
