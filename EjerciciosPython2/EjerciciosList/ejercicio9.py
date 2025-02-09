#Generar una lista de tuplas que consten únicamente de los números coincidentes en estas listas
#  list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. El resultado se vería así (4,4), (12,12)

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [2, 7, 1, 12]
result = []
for i in list_a:
    if i in list_b:
        result.append((i, i))
print(result)