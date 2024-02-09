import psycopg2

def tabla(connection,conn):

        sql = '''  
                CREATE TABLE IF NOT EXISTS SERIES(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        genero VARCHAR(255) NOT NULL,
                        autor VARCHAR(255) NOT NULL,
                        fechaInicio VARCHAR NOT NULL,
                        fechaFin VARCHAR(255) NOT NULL
                )
        '''


        connection.execute(sql)

        conn.commit()
        print("Tabla Creada")