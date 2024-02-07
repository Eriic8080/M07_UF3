#Demanar a l’usuari que posi entre 1 i 3 paraules. Al executar el programa, 
#mostrarà la/es paraula/es indicada/es per l’usuari,
#indicar quants caràcters té i indicar el primer, i l’últim caràcter.
contador = 0
palabras = input("Palabras a introducir 1, 2 o 3: ")

while True:
    a = input("Introduce una palabra ")

    print("La palabra es: "+a+" Tiene "+str(len(a))+" caracteres, su primera letra es :"+a[0]+" y su ultima letra es: "+a[len(a)-1])

    contador+=1
    
    if(contador == int(palabras)):
        break
    