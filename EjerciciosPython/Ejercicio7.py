"""
Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La función recibe un listado que contiene pares, representando cada jugada.
- El par puede contener combinaciones de "R" (piedra), "P" (papel)  o "S" (tijera).
- Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".

"""
def quien_gana_mas_partidas(jugadas):
    victorias = {"Player 1": 0, "Player 2": 0}
    reglas = {("R", "S"): "Player 1", ("S", "P"): "Player 1", ("P", "R"): "Player 1",
              ("S", "R"): "Player 2", ("P", "S"): "Player 2", ("R", "P"): "Player 2"}
    
    for jugada1, jugada2 in jugadas:
        if jugada1 != jugada2:
            victorias[reglas[(jugada1, jugada2)]] += 1
    
    return "Tie" if victorias["Player 1"] == victorias["Player 2"] else ("Player 1" if victorias["Player 1"] > victorias["Player 2"] else "Player 2")

jugadas = [("R", "S"), ("S", "R"), ("P", "S")]
resultado = quien_gana_mas_partidas(jugadas)
print(resultado)  