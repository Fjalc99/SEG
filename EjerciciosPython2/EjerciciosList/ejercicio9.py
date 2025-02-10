#Generar una lista de tuplas que consten únicamente de los números coincidentes en estas listas
#  list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. El resultado se vería así (4,4), (12,12)


list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [2, 7, 1, 12]


def obtener_tuplas_coincidentes(lista_a, lista_b):
    result = []
    for i in lista_a:
        if i in lista_b:
            result.append((i, i))
    return tuple(result)

result = obtener_tuplas_coincidentes(list_a, list_b)

print(result)