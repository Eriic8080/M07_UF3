import psycopg2
def leer(connection,conn):

        sql = '''
                Select * from SERIES
            '''


        connection.execute(sql)
        conn.commit()

        #Con el fetchall() recupero los datos de la consulta y los guardo en una variable
        series = connection.fetchall()

        #Aqui recorro la variable con todos los datos de la tabla SERIES para printar todas las linias que hay 
        for linia in series:
            print(linia)        