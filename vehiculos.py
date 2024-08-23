class Vehiculos:
    def __init__(self, marca, modelo, vm, color, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = vm
        self.velocidad_actual = 0
        self.color = color
        self.kilometraje = kilometraje

    def acelerar(self, velocidad):
        try:
            if self.velocidad_actual+velocidad >= self.velocidad_maxima:
                self.velocidad_actual = self.velocidad_maxima
            else:
                self.velocidad_actual = self.velocidad_actual + velocidad
            print('Aceleramos el auto en '+str(velocidad)+' ahora nuestra velocidad es de '+str(self.velocidad_actual))
        except:
            print('La aceleracion solo acepta datos numericos')
    def frenar(self, velocidad):
        if self.velocidad_actual - velocidad <=0:
            self.velocidad_actual = 0
        else:
            self.velocidad_actual -= velocidad
        print('frenamos el auto en '+str(velocidad)+' ahora nuestra velocidad es de '+str(self.velocidad_actual))

    def pintar(self,color):
        self.color = color
        print('Ahora el auto es de color '+self.color)


class Automoviles(Vehiculos):
    pass


mi_auto = Automoviles('Jeep','Renegade',180,'blanco',343894)
mi_auto.acelerar(20)
mi_auto.acelerar(1100)
mi_auto.frenar(30)
mi_auto.frenar(200)
mi_auto.pintar('Azul')
mi_auto.acelerar('banana')
mi_auto.acelerar(10)