#Crear un arxiu on caldrà endevinar el número escollit pel programa entre 1 i 100.
#Cada vegada que l’usuari hi posi un número, caldrà indicar si és més petit o més gran fins que encerti
#i el missatge haurà d’indicar que ha encertat. Indicar també el número d’intents.
import random


numeroAdivinar = random.randint(1, 100)

while True:
    numero = int(input("Introduce un numero: "))

    while numero>100 or numero<0:
        numero = int(input("Numero introducido incorrecto tiene que ser entre 0-100: "))

    if(numero > numeroAdivinar):
        print("Numero introducido demasiado grande")
    elif(numero==numeroAdivinar):
        print("Numero Adivinado !!!")
        break
    else:
        print("Numero introducido demasiado pequeño")
