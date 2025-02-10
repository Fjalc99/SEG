#Encuentra todos los números del 1 al 1000 que incluyan entre sus cifras al menos un 3.

def numeros_con_tres(rango):
    numeros = []
    for i in rango:
        if '3' in str(i):
            numeros.append(i)
    return numeros

rango = range(1, 1000)
numeros = numeros_con_tres(rango)
for numero in numeros:
    print(numero)