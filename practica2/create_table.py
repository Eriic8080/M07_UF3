import psycopg2

def tabla(connection,conn):

        sql = '''  
                CREATE TABLE SERIES(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        genero VARCHAR(255) NOT NULL,
                        fechaInicio BIGINT NOT NULL,
                        fechaFin VARCHAR(255) NOT NULL
                )
        '''


        connection.execute(sql)

        conn.commit()
        print("Tabla Creada")