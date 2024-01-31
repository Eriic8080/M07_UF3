"""
Demanar a l’usuari que introdueixi 10 números separats per un espai. 
Al acabar, el programa els introduirà en una tupla i els ordenarà (major o menor, com volgueu),
mostrant per pantalla el contingut de la tupla.
"""

numeros  = input("Introduce 10 numeros con espacios: ")

while len(numeros) > 20:
   numeros  = input("ERROR: Máximo se pueden introducir 10 numeros: ")
 
#El split() me separa el texto por espacios 
numeros = [int(x) for x in numeros.split()]

#Con el sorted lo ordeno ascendentemente  y si quisiera hacer-lo fuera de tuple seria .sort()
ordenado = tuple(sorted(numeros))

print(ordenado)


