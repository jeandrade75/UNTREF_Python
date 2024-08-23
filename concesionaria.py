def elegir_marca():
    ford = 15000
    chevrolet = 14000
    fiat = 11000
    #Primero pregunto por la marca
    precio = 0
    correcto = False
    while correcto == False:
        correcto = True
        marca = input('Ingrese marca de auto: ')
        if marca == 'ford':
            precio =ford
        elif marca == 'chevrolet':
            precio =chevrolet
        elif marca == 'fiat':
            precio =fiat
        else:
            print('La marca no existe')   
            correcto = False
    return precio
def elegir_color():
    p_color = 0
    color = input('Ingrese color:')
    if color != 'blanco' and color!='rojo' and color!='negro':
        p_color = 1500
    return p_color

def fabricacion():
    a_fab = int('Ingrese a;o de fabricacion: ')
    antiguedad = 2024 - a_fab
    return antiguedad*550
otro_cliente = 'y'
while otro_cliente == 'y':
    precio = elegir_marca()
    #Segundo pregunto por el color
    precio += elegir_color()
    #tercero pregunto a;o de fabricacion
    precio -= fabricacion()
    if precio < 1000:
        precio = 1000
    print('Precio final: '+str(precio))
    otro_cliente = input('Hay otro cliente?')