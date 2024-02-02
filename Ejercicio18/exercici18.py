"""
Demanar a l’usuari posar 2 paraules. Afegir aquestes a una tupla i
mostrar per pantalla quantes vegades apareix cada lletra.
"""

palabra1 = input("Introduce una palabra: ")

palabra2 = input("Introduce otra palabra: ")

tupla = (palabra1,palabra2)
print(tupla)

#Variables para almacenar el num de letras que aparecen para la palabra 1 y 2
letrasPalabra1 ={}
letrasPalabra2 = {}

#Con el for recorro la palabra caracter por caracter
for letra in palabra1:
#La letra que haya la paso a minusculas
    letra = letra.lower()
#Creo una variable que usa el metodo count que lo que hace es contar el numero de letras que hay sobre 
#la letra indicada a buscar sobre la variable palabra1

    contar = palabra1.count(letra)

#Una vez contada se guarda en el array creado pasando-le la letra que es y el numero de veces que sale 
    letrasPalabra1[letra] = contar

for letra in palabra2:
    letra = letra.lower()

    contar = palabra2.count(letra)

    letrasPalabra2[letra] = contar

print("Palabra 1:")
#Para mostar-lo hacemos un for que vaya recorriendo el array y que tenga 2 variables 
#que asuman el valor de letra y la otra su valor como en este caso letra y num
for letra, num in letrasPalabra1.items():
    print(f"La letra '{letra}' aparece {num} veces")

print("Palabra 2:")
    #Ademas para que nos deje printar-lo tenemos que usar printF para que nos deje usar las {} para meter los valores
for letra, num in letrasPalabra2.items():
    print(f"La letra '{letra}' aparece {num} veces")