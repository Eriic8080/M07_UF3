#Demanar a l’usuari que posi dues paraules. Al executar el programa, 
#mostrarà per pantalla les dues paraules amb els dos primers caràcters de cada paraula intercanviats. 
#Exemple: Quatre Camins passaria a Caatre Qumins.

palabra1 = input("Introduce una Palabra: ")

palabra2 = input("Introduce la segunda Palabra: ")

#Con los :  indico que me guarde los caracteres de la posicion 0-1 ya lo la 2 no lo pilla
cambio1 = palabra1[0:2]

cambio2 = palabra2[0:2]


palabra1 = palabra1.replace(palabra1[0:2],cambio2)
palabra2 = palabra2.replace(palabra2[0:2],cambio1)



print("Palabra 1: "+palabra1)
print("Palabra 2: "+palabra2)
