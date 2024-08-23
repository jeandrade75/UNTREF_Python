a = 10
b = 20
c= a * b

print(c)

d= 'Hola'
e= 'Pepe'
f = '¿Como estas?'
g= d +' '+e+' '+f
print(g)


edad = int(input('Ingrese su edad: '))

mensaje = ''

if      edad<18:
        mensaje= 'Es menor'
elif    edad>60:     
        mensaje= 'Es jubilado' 
else:   mensaje= 'Es mayor'

print(mensaje)