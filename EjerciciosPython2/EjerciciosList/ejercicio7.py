#Obtén solamente los números en una oración como 'En 1984 hubo 13 casos de protesta con más de 1000 asistentes'

def obtener_numeros(texto):
    numeros = []
    for i in texto.split():
        if i.isnumeric():
            numeros.append(int(i))
    return numeros

texto = 'En 1984 hubo 13 casos de protesta con más de 1000 asistentes'
numeros = obtener_numeros(texto)
print(numeros)
