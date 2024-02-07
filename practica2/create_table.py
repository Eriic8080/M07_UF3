from conn import conectar
def tabla():
        sql = '''
                CREATE TABLE SERIES(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        genero VARCHAR(255) NOT NULL,
                        fechaInicio BIGINT NOT NULL,
                        fechaFin VARCHAR(255) NOT NULL
        )'''

        connection = conectar()
        connection.execute(sql)

        conn.commit()
        print("PROCESSO HECHO")