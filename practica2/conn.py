import psycopg2
def conectar():

        conn = psycopg2.connect(
            database = "practica2",
            user = 'eric',
            password = 'eric',
            host = 'localhost',
            port = '5432'
        )

        connection = conn.cursor()

        print("Conexion hecha")

        return connection, conn



