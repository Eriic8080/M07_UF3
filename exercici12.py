"""
Crear una tupla amb els mesos de l’any.
Demanar a l’usuari que posi un número entre 0 i 12 i mostrar per pantalla 
el mes corresponent al número indicat per l’usuari. El programa finalitza només 
quan l’usuari posa 0.
"""

num = 1

meses = ("EXIT","Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

while num != 0:
    num = int(input("Introduce un numero entre 0-12: "))
    while num > 12 or num < 0:
        num = int(input("ERROR: El numero a introducier tiene que ser entre 0-12: "))

    print(meses[num])



