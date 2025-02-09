#Obtén solamente los números en una oración como 'En 1984 hubo 13 casos de protesta con más de 1000 asistentes'

Texto = 'En 1984 hubo 13 casos de protesta con más de 1000 asistentes'
numeros = []
for i in Texto.split():
    if i.isnumeric(): 
        numeros.append(int(i)) 

print(numeros)  
