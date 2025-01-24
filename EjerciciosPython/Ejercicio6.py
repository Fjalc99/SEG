"""

Crea una función que reciba dos array, un booleano y retorne un array.
- Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
- Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""

def compare_arrays(array1, array2, booleano):
    if booleano:
        return [elemento for elemento in array1 if elemento in array2]
    else:
        return [elemento for elemento in array1 if elemento not in array2] + [elemento for elemento in array2 if elemento not in array1]
    

array1 = input("Inserte un array: ").split()

array2 = input("Inserte un array: ").split()

booleano = input("Inserte un booleano: ")

print(compare_arrays(array1, array2, booleano))

