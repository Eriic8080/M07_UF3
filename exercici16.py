"""
Demanar a l’usuari una frase. El programa eliminarà els espais
i s'afegirà a una tupla. Mostrar per pantalla el contingut de la tupla.
"""

frase = input("Introduce una frase: ")

tupla = tuple(frase.split())

print(tupla)