import MySQLdb as mdb
import sys
import argparse

def copiaDatos(data, nombre):
        fout = open (nombre, 'wb')
        with fout:
                fout.write(data)

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

conexion = mdb.connect('host', 'usuario', 'passwd', 'dbname')

parser = argparse.ArgumentParser()
parser.add_argument("file_name", help="CSV con IDs y referencias", type=str)
args = parser.parse_args()
fichero = args.file_name

with open (fichero, 'r') as listaIDs:
    n = 1
    total = file_len(fichero)
    for line in listaIDs:
        id = line.split(';')[0].rstrip()
        referencia = line.split(';')[1].rstrip()
        with conexion:
            cur = conexion.cursor()
            cur2 = conexion.cursor()
            cur.execute("SELECT datos FROM somewhere WHERE id=" + id)
            cur2.execute("SELECT nombre FROM somewhereelse WHERE id=" + id)
            nombre = referencia + '_' + id + '_' + str(cur2.fetchone()[0])
            progreso = '(' + str(n) + '/' + str(total) + ') Obteniendo ' + nombre
            sys.stdout.write('%s\r' % progreso)
            data = cur.fetchone()[0]
            copiaDatos(data, nombre)
        n += 1
