#Encuentra todas las palabras en una cadena que tengan menos de 4 letras


def encontrar_palabras_cortas(texto):
    return [palabra for palabra in texto.split() if len(palabra) < 4]


texto = "viva el betis bueno, ole ole betis"
print(encontrar_palabras_cortas(texto))