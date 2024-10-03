from vehiculos import Vehiculos

class Camiones(Vehiculos):
    def __init__(self, marca, modelo, vm, color, kilometraje,carga):
        super().__init__(marca,modelo,vm,color,kilometraje)
        self.carga = carga
    def cargar(self,carga):
        self.carga +=carga
    def descargar(self,carga):
        self.carga -=carga