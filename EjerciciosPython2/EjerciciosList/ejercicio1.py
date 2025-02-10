#Encuentra todos los números del 1 al 1000 que sean divisibles por 7

def numeros_divisibles_por_siete(rango):
    numeros = []
    for i in rango:
        if i % 7 == 0:
            numeros.append(i)
    return numeros

rango = range(1, 1000)
numeros = numeros_divisibles_por_siete(rango)
for numero in numeros:
    print(numero)