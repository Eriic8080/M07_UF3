import psycopg2

try:
    conn = psycopg2.connect(
        database = "practica2",
        user = 'eric',
        password = 'eric',
        host = 'localhost',
        port = '5432'
    )

    connection = conn.cursor()

    sql = '''CREATE TABLE USERS2(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    SURNAME VARCHAR(255) NOT NULL,
                    AGE BIGINT NOT NULL,
                    EMAIL VARCHAR(255) NOT NULL
    )'''


    connection.execute(sql)

    conn.commit()

except (Exception, psycopg2.Error) as error:
    print("Error",error)

finally:
    conn.close()
