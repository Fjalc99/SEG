#Crea una lista de todas las consonantes de la cadena “A los yaks amarillos les gusta gritar y bostezar y ayer cantaban mientras comían ñames asquerosos”

cadena = "A los yaks amarillos les gusta gritar y bostezar y ayer cantaban mientras comían ñames asquerosos"
consonantes = []
for i in cadena:
    if i.lower() not in "aeiouáéíóú":
        consonantes.append(i)  
print(consonantes)