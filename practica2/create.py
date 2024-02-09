import psycopg2

def crearDatos(connection,conn):

        sql = '''
                Insert into SERIES (name,genero,autor,fechaInicio,fechaFin)
                    VALUES ('THE WALKING DEAD','SUSPENSE','ERIC','31 de octubre de 2010','20 de noviembre de 2022')
            '''


        connection.execute(sql)

        conn.commit()
        print("Datos Introducidos Correctamente")