#Crea una lista de todas las consonantes de la cadena “A los yaks amarillos les gusta gritar y bostezar y ayer cantaban mientras comían ñames asquerosos”

def obtener_consonantes(cadena):
    consonantes = []
    for i in cadena:
        if i.lower() not in "aeiouáéíóú":
            consonantes.append(i)
    return consonantes

cadena = "A los yaks amarillos les gusta gritar y bostezar y ayer cantaban mientras comían ñames asquerosos"
consonantes = obtener_consonantes(cadena)
print(consonantes)