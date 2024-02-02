"""
Igual que l’anterior però a la tupla afegir la frase sense els caràcters repetits 
i mostrar el contingut de la tupla. Exemple: Usuari indica la paula caracteristica.
Es mostra per pantalla carteis.
"""

frase = input("Introduce una frase: ")

frase = frase.split()

# Primero pongo la tupla en minusculas, despues con filter(str.isalpha) filtro que sean letras,
# despues con dict.fromkeys crea un diccionario que se guarda que letras han salido para no repetir-las
# y por ultimo el join se encarga de juntar las letras que no estan repetidashola
sinDuplicados = [''.join(sorted(set(palabra),key = palabra.index))for palabra in frase]

print(sinDuplicados)
