#Encuentra los números comunes en dos listas (sin usar una tupla o conjunto) lista_a = 1, 2, 3, 4, lista_b = 2, 3, 4, 5

def numeros_comunes(lista_a, lista_b):
    comunes = []
    for i in lista_a:
        if i in lista_b:
            comunes.append(i)
    return comunes

lista_a = [1, 2, 3, 4]
lista_b = [2, 3, 4, 5]

comunes = numeros_comunes(lista_a, lista_b)
for numero in comunes:
    print(numero)