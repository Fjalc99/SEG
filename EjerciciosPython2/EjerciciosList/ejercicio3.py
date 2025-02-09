#Contar el número de espacios en una cadena

cadena = "Hola mundo"
contador = 0
for i in cadena:
    if i == " ":
        contador += 1
print(contador)