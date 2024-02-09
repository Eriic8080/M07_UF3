import psycopg2

def borrarDatos(connection,conn):

        sql = '''
                DELETE from SERIES 
                    WHERE name = 'THE WALKING DEAD'
            '''


        connection.execute(sql)

        conn.commit()
        print("Datos Eliminados Correctamente")