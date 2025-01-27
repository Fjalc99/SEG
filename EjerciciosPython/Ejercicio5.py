"""
Crea una función que evalúe si un/a atleta ha superado correctamente una carrera de obstáculos.
- La función recibirá dos parámetros:
     - Un array que sólo puede contener String con las palabras "run" o "jump"
     - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
- La función imprimirá cómo ha finalizado la carrera:
     - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no variará el símbolo de esa parte de la pista.
     - Si hace "jump" en "_" (suelo), se variará la pista por "x".
     - Si hace "run" en "|" (valla), se variará la pista por "/".
- La función retornará un Boolean que indique si ha superado la carrera. Para ello tiene que realizar la opción correcta en cada tramo de la pista.

"""


def evaluar_carrera(acciones, pista):
    
    pista_lista = list(pista)
    
 
    for i in range(len(acciones)):
      
        accion = acciones[i]
        tramo = pista_lista[i]
        
   
        if accion == "run":
            if tramo == "|":
                pista_lista[i] = "/" 
            elif tramo == "_":
                continue 
        elif accion == "jump":
            if tramo == "_":
                pista_lista[i] = "x"  
            elif tramo == "|":
                continue  
    

    carrera_exitosa = all(tramo != "x" and tramo != "/" for tramo in pista_lista)
    

    pista_resultado = ''.join(pista_lista)
    

    print(f"Pista resultante: {pista_resultado}")
    
 
    return carrera_exitosa


acciones = ["run", "jump", "run", "run"]
pista = "_|_|_"
resultado = evaluar_carrera(acciones, pista)
print("¿Carrera superada?", resultado)
