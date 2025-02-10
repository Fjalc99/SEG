#Contar el número de espacios en una cadena

def contar_espacios(cadena):
    contador = 0
    for i in cadena:
        if i == " ":
            contador += 1
    return contador

cadena = "Hola mundo"
contador = contar_espacios(cadena)
print(contador)