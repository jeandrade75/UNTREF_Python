#Crear una funcion en la que , al ingresar 5 valores
#por terminal, retornara el valor mas alto y luego lo
#mostrara en terminal

def encontrar_valor_maximo():
    valores = []
    
    for i in range(5):
        valor = float(input(f"Ingrese el valor {i+1}: "))
        valores.append(valor)
    
    valor_maximo = max(valores)
    
    print(f"El valor más alto ingresado es: {valor_maximo}")

# Llamar a la función
encontrar_valor_maximo()
