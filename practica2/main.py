import psycopg2

from conn import conectar
from create_table import tabla
from create import crearDatos
from read import leer
from update import modificar
from delete import borrarDatos

try:
    #Connexion a la BD
    print("Conexion:")
    connection, conn = conectar()
    print()
    
    #Funcion para crear una tabla
    print("Creació tabla:")
    tabla(connection, conn)
    crear = input("Continuar?: ")
    print()

    if(crear == "si"):

        #Funcion Introducir datos a la tabla
        print("Insertar Datos:")
        crearDatos(connection, conn)
        insertar = input("Continuar?: ")
        print()

        if(insertar == 'si'):

            #Funcion leer tabla
            print("Lectura de la tabla:")
            leer(connection, conn)
            lectura = input("Continuar?: ")
            print()

            if(lectura == "si"):

                #Funcion para modificar Datos de la tabla
                modificar(connection,conn)
                print()
                #Printamos otra vez los datos para ver los cambios
                leer(connection, conn)
                borrar = input("Continuar?: ")
                print()

                if(borrar == "si"):

                    #Funcion para ELIMINAR Datos de la tabla
                    borrarDatos(connection, conn)
                    print()

                else:
                    print("FIN")
            else:
                print("FIN")
        else:
            print("FIN")

    else:
        print("FIN")
    

except (Exception, psycopg2.Error) as error:

    print("Error",error)

finally:
    conn.close()


