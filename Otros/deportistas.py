#Crear clase Personas
#- Nombre
#- Apellido
#- Edad
#- Estado civil
#- velocidad = 0
#- Velocidad Maxima
#- Caminar: Mostrar un mensaje que estan caminando. Velocidad + 0.1km
#- Hablar: metodo donde le pasan un parametro y retorna el texto o lo imprime
#- Casarse, divorciarse, o enviudar (cambia el estado civil)

# Tres clases que heredan
# 1- Basketbolistas. Aparte tienen Numero de jugador, equipo y numero de camiseta
# Los basketbolistas pueden ser transferidos a otros equipos, y pueden cambiar de numero de camiseta
# En el main, van a crear varios jugadores, van a ir haciendo operaciones. Van a listar los jugadores que
# juegan en Ferro

# 2- Tenistas. Tienen aparte ranking ATP, marca de raqueta, un record de partidos ganados y perdidos y un rival
# Los rivales, son una lista de otros tenistas.

# 3- Velocistas. Tienen que tener club al que pertenecen, Mejor marca en 100 metros, en 200 m.
# pueden correr carreras, y si el tiempo supera la mejor marca, esa marca pasa a ser la mejor.

# 4- Crear dos objetos de tipo basketbolista.
# Hay una propiedad que indica si tiene la pelota o no.
# Tiene que haber un metodo que sea pasar pelota.

class Personas:
    def __init__(self, nombre, apellido, edad, estado_civil, velocidad_maxima):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.estado_civil = estado_civil
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def caminar(self): 
        self.velocidad_actual += 0.1
        print('La persona caminó ' + str(self.velocidad_actual) + ' kms')
    
    def hablar(self, habla):
        print(self.nombre + ' dice ' + habla)
    
    def cambio_estado_civil(self, estado_civil):
        try:
            estados = {'casarse':'Casado', 'divorciarse':'Divorciado','enviudar':'Viudo'}
            estado = estado_civil.lower()
            if estados[estado] == self.estado_civil:
                print('Esta repitiendo el estado')
            else:
                self.estado_civil = estados[estado]
                print('Estado actual: '+self.estado_civil)
        except:
            print('No existe ese estado civil')


persona_1 = Personas('Jazmin', 'Rivas', 41, 'casada', 10)
persona_1.hablar('Hola')
persona_1.caminar()
persona_1.caminar()
persona_1.cambio_estado_civil('casarse')
print(persona_1.estado_civil)
persona_1.cambio_estado_civil(1)
persona_1.cambio_estado_civil('dsfdjflkdjflkdsjflksd')
persona_1.cambio_estado_civil('enViudar')
persona_1.cambio_estado_civil('CasArSe')