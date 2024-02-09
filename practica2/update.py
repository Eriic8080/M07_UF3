import psycopg2

def modificar(connection,conn):

        sql = '''
                UPDATE SERIES set autor = 'AMC Networks' WHERE autor = 'ERIC'
            '''


        connection.execute(sql)

        conn.commit()
        print("Datos Modificados Correctamente")