"""
Crear un diccionari on la clau (key) sigui un nom i el valor (value) l’edat. 
S’haura de demanar a l’usuari que posi contactes (noms i edats).
Si algun nom es repeteix no s’fageirà al diccionari (indicant-ho a l’usuari). 
Es deixarà d’inserir contactes quan l’usuari indiqui que no vol afegir-ne més.
"""

diccionari = {}

while True:
    nombre = input("Introduce un Nombre (Para salir esciribir: no mes): ")
    if nombre.lower() == 'no mes':
        break

#con el .keys() lo que le digo la clave que en este caso son los nombres y con el for voy recorriendo todos los nombre que tiene el array
    for nom in diccionari.keys():
        #Aqui comparo los nombres que hay en el array con el nuevo introducido para que no hayan repetidos
        while nombre == nom:
            print("Error ese nombre ya ha sido introducido")
            nombre = input("Introduce otro nombre distinto: ")
            

    edat = input("Introduce una edat: ")

    diccionari[nombre] = edat

print(diccionari)
