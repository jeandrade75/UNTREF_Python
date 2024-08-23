""" Uniendo Conceptos:
Creamos una estructura for para ingresar diferentes edades,
y posteriormente una segunda estructura for para mostrar
en terminal los valores mayores a 30. """

def ingresar_edades(n):
    edades = []
    print(f"Ingrese {n} edades:")

    # Primer for para ingresar las edades
    for i in range(n):
        edad = int(input(f"Ingrese la edad {i+1}: "))
        edades.append(edad)

    return edades

def mostrar_mayores_a_30(edades):
    print("\nEdades mayores a 30:")

    # Segundo for para mostrar las edades mayores a 30
    for edad in edades:
        if edad > 30:
            print(edad)

# Ejemplo de uso
n = int(input("¿Cuántas edades va a ingresar? "))
edades = ingresar_edades(n)
mostrar_mayores_a_30(edades)