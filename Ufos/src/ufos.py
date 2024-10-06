import csv
from datetime import datetime
from math import sqrt
from collections import namedtuple


Avistamiento = namedtuple('Avistamiento',['fechahora', 'ciudad', 'estado', 'forma', 'duracion', 'comentarios', 'latitud', 'longitud'])

def lee_avistamiento(fichero):
    res = []
    print(res)
    with open(fichero, encoding = 'utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        (next(reader))

        print(reader)
        for x in reader:
            fecha_hora = x[0]
            fechahora = datetime.strptime(fecha_hora, '%Y-%m-%d %H:%M:%S')
            ciudad = x[1]
            estado = x[2]
            forma = x[3]
            duracion= int(x[4])
            comentarios = x[5]
            latitud = float(x[6])
            longitud = float(x[7])
            tupla = Avistamiento(fechahora,ciudad,estado, forma, duracion, comentarios, latitud, longitud)
            print(tupla)
            res.append(tupla)


    print(res)
    return res


