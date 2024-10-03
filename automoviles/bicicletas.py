from vehiculos import Vehiculos


class Bicicletas(Vehiculos):
    def __init__(self, marca, modelo, color, rodado):
        super().__init__(marca,modelo,0,color,0)
        self.rodado = rodado
    def acelerar(self, velocidad):
        self.velocidad_actual += velocidad
        print('Empiezo a pedalear, y ahora voy a '+str(self.velocidad_actual))
    def frenar(self, velocidad):
        self.velocidad_actual -= velocidad
        print('aprieto el freno, y ahora voy a '+str(self.velocidad_actual))