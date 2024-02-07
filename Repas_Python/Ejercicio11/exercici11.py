#Demanar a l’usuari un nùmero entre 10 i 100. Posar els números a una tupla desde 1 fins 
#al número indicat per l’usuari. Exemple: usuari indica 34, es crea una tupla i es mostra per 
#pantalla els números de l’1 al 34 (imprimint la tupla).

num = int(input("Introduce un numero entre 10-100: "))

while num<10 | num >100:
    num = input("El numero tiene que ser entre 10-100: ")

#tuple almacena la secuanecia de numeros creados por el range(numInicial, numFinal de la generacion de secuencia) 
tu = tuple(range(1, num+ 1))

print(tu)
