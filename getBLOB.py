import MySQLdb as mdb
import sys

def copiaDatos(data, nombre):
        fout = open (nombre, 'wb')
        with fout:
                fout.write(data)

conexion = mdb.connect('host', 'user', 'pass', 'dbname')
id = str(sys.argv[1])

with conexion:
        cur = conexion.cursor()
        cur2 = conexion.cursor()
        cur.execute("SELECT some_binary FROM somewhere WHERE id=" + id)
        cur2.execute("SELECT some_binary_name FROM somewhere WHERE id=" + id)
        nombre = str(cur2.fetchone()[0])
        data = cur.fetchone()[0]
        copiaDatos(data, nombre)
