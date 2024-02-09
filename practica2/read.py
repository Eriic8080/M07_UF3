import psycopg2

def leer(connection,conn):

        sql = '''
                Select * from SERIES
            '''


        connection.execute(sql)
        conn.commit()

        series = conn.feachall()
        print("Lectura Hecha")
        print(series)
        