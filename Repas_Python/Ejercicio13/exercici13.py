"""
Demanar a l’usuari un número de l’1 al 10 i mostrar per pantalla 
la seva taula de multiplicar fins el 10. Exemple: l’usuari marca 3, 
es mostra per pantalla: 3,6,9,12,15,18,21,24,27 i 30
"""

num = int(input("Introduce un numero del 1-10: "))

while num >10 or num <1:
    num = int(input("ERROR: El numero a introducir tiene que ser entre 1-10: "))

for i in range(1,11):
    if i == 9:
        print(num*i,end=' i ')
    elif i == 10:
        print(num*i)
    else:
        #Con el end hago que no tenga salto de linia el print() y le indico que quiero una ', ' despues de cada printeo de la multiplicación
        print(num*i,end=', ')

