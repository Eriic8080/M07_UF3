"""
El mateix que l’anterior exercici, però sense demanar un màxim de números.
L’usuari indicarà quan ha acabat posant un 0.
"""

numeros = []
while True: 
    numero = int(input("Introduce un numero: "))
    if numero == 0:
        break
    numeros.append(numero)


#Con el sorted lo ordeno ascendentemente  y si quisiera hacer-lo fuera de tuple seria .sort()
ordenado = tuple(sorted(numeros))

print(ordenado)
