#Encuentra los números comunes en dos listas (sin usar una tupla o conjunto) lista_a = 1, 2, 3, 4, lista_b = 2, 3, 4, 5

lista_a = [1, 2, 3, 4]
lista_b = [2, 3, 4, 5]

for i in lista_a:
    if i in lista_b:
        print(i)
