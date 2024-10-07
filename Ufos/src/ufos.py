import csv
from datetime import  datetime
from collections import namedtuple

# Creacion de una tupla con nombre para los avistamientos
avistamiento = namedtuple('avistamiento',
                                  ['fechahora', 'ciudad','estado', 'forma',
                                   'duracion', 'comentario', 'latitud', 'longitud'])
def leeAvistamientos(fichero):
    resultado = []
    with open(fichero, encoding='UTF-8') as f:
        reader = csv.reader(f, delimiter=",")
        (next(reader))


        for linea in reader:
            fecha_hora = linea[0]
            fechahora = datetime.strptime(fecha_hora, '%m/%d/%Y %H:%M')
            ciudad = linea[1]
            estado = linea[2]
            forma = linea[3]
            duracion = int(linea[4])
            comentario = linea[5]
            latitud = float(linea[6])
            longitud = float(linea[7])
            tupla = avistamiento(fechahora, ciudad, estado, forma, duracion, comentario, latitud, longitud)
            resultado.append(tupla)
        return resultado


