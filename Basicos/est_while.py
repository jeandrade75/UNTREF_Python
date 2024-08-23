#El while lo va a ejecutar mientras la condicion sea True

#Tenemos un motor que en cada vuelta recorre 150 mts
#El motor va a parar a las 10 vueltas

vueltas=0
distancia=0

while vueltas<10:
    distancia+=150
    vueltas+=1
    print('Distancia: '+str(distancia))

print ('Termino de andar')
