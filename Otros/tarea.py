#Hay una concesionaria de autos
#Se venden 3 tipos de auto
#Ford, Chevrolet, Fiat
#Los autos ford valen 15000 dolares
#Los autos chevrolet valen 14000 dolares
#Los autos Fiat valen 11 dolares
#Los autos vienen en color blanco, rojo o negro
#SI el color que quiere el cliente es distinto, se le agregan 1500 dolares
#Tambien pueden ser autos usados. Por cada a;o hacia atras, se descuentan 550 dolares.
#El menor valor va a ser 1000 dolares
#Van a venir n clientes a la concesionaria
#A cada cliente se le va a pedir: auto, color, a;o
#Se debe informar todos estos datos mas el valor final del auto
#en caso de que por cualquier motivo no se pueda vender el auto. Debe informarse en 
#lugar del valor, que no se puede concretar la venta.


def calcular_precio_auto(marca, color, anio, anio_actual=2024):
    # Definir precios base
    precios = {'Ford': 15000, 'Chevrolet': 14000, 'Fiat': 11}
    
    # Verificar si la marca del auto es válida
    if marca not in precios:
        return "No se puede concretar la venta: Marca no disponible"
    
    # Precio inicial basado en la marca
    precio_base = precios[marca]
    
    # Verificar si el color es válido
    colores_validos = ['blanco', 'rojo', 'negro']
    if color not in colores_validos:
        precio_base += 1500  # Agregar costo extra por color no estándar
    
    # Calcular la depreciación del auto usado
    años_usado = anio_actual - anio
    descuento = años_usado * 550
    
    # Calcular el precio final con un valor mínimo de 1000 dólares
    precio_final = max(precio_base - descuento, 1000)
    
    return precio_final

def procesar_clientes(clientes):
    for cliente in clientes:
        auto, color, anio = cliente['auto'], cliente['color'], cliente['anio']
        precio_final = calcular_precio_auto(auto, color, anio)
        
        # Imprimir los detalles del cliente y el precio final del auto
        print(f"Cliente quiere: {auto} de color {color} del año {anio}")
        if isinstance(precio_final, str):
            print(precio_final)
        else:
            print(f"Valor final del auto: ${precio_final}\n")

# Ejemplo de clientes
clientes = [
    {'auto': 'Ford', 'color': 'blanco', 'anio': 2020},
    {'auto': 'Chevrolet', 'color': 'verde', 'anio': 2018},
    {'auto': 'Fiat', 'color': 'negro', 'anio': 2022},
    {'auto': 'Toyota', 'color': 'rojo', 'anio': 2019},  # Marca no disponible
    {'auto': 'Ford', 'color': 'azul', 'anio': 2000},  # Color no estándar y depreciación
]

procesar_clientes(clientes)
