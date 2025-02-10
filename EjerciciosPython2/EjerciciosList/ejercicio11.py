#Utiliza una comprensión de lista anidada para encontrar todos los números del 1 al 1000 que sean 
# divisibles por cualquier dígito excepto 1 (2-9)


def obtener_numeros_divisibles():
    return [
        n for n in range(1, 1001) 
        if {int(d) for d in str(n)} & {2, 3, 4, 5, 6, 7, 8, 9}
        and any(n % int(d) == 0 for d in str(n) if d not in '01')
    ]

numeros_divisibles = obtener_numeros_divisibles()
print(numeros_divisibles)
