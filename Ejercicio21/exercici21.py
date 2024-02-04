""""
Demanar a l’usuari que posi 10 números separats per espais. 
Afegir aquests números a una llista. Calcular la suma de tots els números i 
la seva mitjana i afegir aquests 2 números a la llista. Mostrar per pantalla la llista.
"""

numeros_str = input("Introduce 10 números separados por espacios: ")

numeros = numeros_str.split()

n = [int(num) for num in numeros]

#Con sum haces la suma de todo los numeros que hay en la lista
suma = sum(n)

media = suma/len(n)

#Con appened introduzco estas variables al array
n.append(suma)
n.append(media)

print("La suma de los numeros introducidos es: "+ str(suma))
print("La media es de: "+ str(media))
print("La lista de los numeros agregando la suma y la media: "+str(n))


