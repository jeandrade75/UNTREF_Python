#Una func
# ion, recibe 5 valores
#Retornar mayor*menor*promedio

def calcular_estadisticas(val1, val2, val3, val4, val5):
    # Crear una lista con los cinco valores
    valores = [val1, val2, val3, val4, val5]
    
    # Calcular el mayor y el menor valor
    mayor = max(valores)
    menor = min(valores)
    
    # Calcular el promedio
    promedio = sum(valores) / len(valores)
    
    return mayor, menor, promedio

# Ejemplo de uso
mayor, menor, promedio = calcular_estadisticas(10, 20, 30, 40, 50)
print(f"Mayor: {mayor}, Menor: {menor}, Promedio: {promedio:.2f}")
