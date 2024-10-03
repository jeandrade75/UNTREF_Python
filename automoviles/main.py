from automoviles import Automoviles
from camiones import Camiones
from bicicletas import Bicicletas

mi_auto = Automoviles('Jeep','Renegade',180,'blanco',343894)
mi_auto.acelerar(20)
mi_auto.acelerar(1100)
mi_auto.frenar(30)
mi_auto.frenar(200)
mi_auto.pintar('Azul')
mi_auto.acelerar('banana')
mi_auto.acelerar(10)

mi_camion = Camiones('Mercedes Benz', '1234', 150,'Rojo',123,1000)
mi_camion.acelerar(100)
mi_camion.frenar(10)
mi_camion.cargar(100)
mi_camion.descargar(50)

mi_bicicleta = Bicicletas('Aurora','Aurorita','Verde',20)
mi_bicicleta.acelerar(10)
mi_bicicleta.frenar(5)