"""
 Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
- Equilibrado significa que estos delimitadores se abren y cierran en orden y de forma correcta.
- Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
- Expresión balanceada: { [ a * ( c + d ) ] - 5 }
- Expresión no balanceada: { a * ( c + d ) ] - 5 }

"""

def delimitadores_equilibrados(expresion):
    
    pila = []
    
    pares_delimitadores = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
   
    delimitadores_apertura = set(pares_delimitadores.values())

    for caracter in expresion:
        if caracter in delimitadores_apertura:
            pila.append(caracter)  
        elif caracter in pares_delimitadores:
            if not pila or pila[-1] != pares_delimitadores[caracter]:
                return False  
            pila.pop()  

    return len(pila) == 0  


if __name__ == "__main__":
    expresion = input("Ingresa una expresión: ")
    if delimitadores_equilibrados(expresion):
        print("La expresión está equilibrada.")
    else:
        print("La expresión no está equilibrada.")