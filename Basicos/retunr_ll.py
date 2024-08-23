#Queremos una funcion que nos indique si un nro es par o inpar

def paridad (num):
    paridad = True
    if num % 2 == 0:
        paridad = True
    else:
        paridad = False
    return paridad

la_paridad= paridad(24)
print(la_paridad) #True

