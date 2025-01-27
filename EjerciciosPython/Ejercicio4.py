"""
Crea una función que reciba un String de cualquier tipo y se encargue de poner en mayúscula la primera letra de cada palabra.
- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

"""
def mayuculas(texto: str):
    texto = texto.split()
    texto = [palabra[0].upper() + palabra[1:] for palabra in texto]
    return " ".join(texto)


texto = input("Inserte un texto: ")
print(mayuculas(texto))