#Obtén el índice y el valor como una tupla para los elementos de la lista “hi”, 4, 8.99, 'apple', ('t,b','n'). El resultado se vería así (índice, valor), (índice, valor)

def obtener_indices_y_valores(lista):
    resultado = []
    for i in range(len(lista)):
        resultado.append((i, lista[i]))
    return resultado

lista = ["hi", 4, 8.99, 'apple', ('t,b','n')]
indices_y_valores = obtener_indices_y_valores(lista)
for tupla in indices_y_valores:
    print(tupla)
        
        
