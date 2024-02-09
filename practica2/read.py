import psycopg2

def leer(connection,conn):

        sql = '''
                Select * from SERIES
        )'''


        connection.execute(sql)

        conn.commit()
        print("Lectura Hecha")