import psycopg2

from conn import conectar
from create_table import tabla
from read import leer

try:
    #Connexion a la BD
    print("Conexion:")
    connection, conn = conectar()
    
    #Funcion para crear una tabla
    print("Creació tabla:")
    tabla(connection, conn)

    #Funcion leer tabla
    print("Lectura de la tabla")
    leer(connection, conn)

except (Exception, psycopg2.Error) as error:

    print("Error",error)

finally:
    conn.close()


