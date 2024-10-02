import math;

#Ejercicio 1

def areaRectangulo (base, altura):
    resultado = base * altura
    return resultado

print(areaRectangulo(15,10))


#Ejercicio 2

def areaCirculo (radio):
    return math.pi * radio**2

print(areaCirculo(5))


#Ejercicio 3

def relacion(a, b):
    if a > b:
        return 1
    else:
        if a < b:
            return -1
        else:
            if a == b:
                return 0
print(relacion(5,10))
print(relacion(10,5))
print(relacion(5,5))

#Ejercicio 4

def intermedio(a, b):
    return (a + b) / 2
print(intermedio(-12,24))


#Ejercicio 5

def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    else:
        return numero
print(recortar(15,0,10))

#Ejercicio 6

def separar(lista):
    lista.sort()
    pares = []
    impares = []

    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    return pares, impares

numeros = [6,5,2,1,7]
pares, impares = separar(numeros)
print("Pares:", pares)
print("Impares:", impares)
