from conn import conectar
try:
    conectar()

except (Exception, psycopg2.Error) as error:
    print("Error",error)

finally:
    conn.close()
