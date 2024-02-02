"""Cal buscar la informació que es demana de la següent list:"""

areas_pis = ['Menjador', 10.15, 'Rebedor', 9.56, 'Habitació1', 12.34, 'Terrassa', 
             15.55, 'Lavabo', 7.98, 'Cuina', 12, 'Habitació2', 12.23]


#Imprimir el segon element

print("Imprimir el segon element: "+str(areas_pis[1]))
print()

#Imprimir l’últim element

print("Imprimir l’últim element: "+ str(areas_pis[len(areas_pis)-1]))
print()

#Imprimir l’àrea de la terrassa

print("Imprimir l’àrea de la terrassa: "+ str(areas_pis[7]))
print()

#Imprimir del primer element al tercer element

    #Con lo puntos le digo que me muestre desde el principo hasta la posicion 2 que seria el elemento 3 
print("Imprimir del primer element al tercer element: "+ str(areas_pis[:3]))
print()

#Imprimir del tercer element a l’últim

print("Imprimir del tercer element a l’últim: "+ str(areas_pis[2:]))
print()

#Imprimir el total de l'àrea de les dues habitacions
print("Area Habitación 1: " + str(areas_pis[5]))
print("Area Habitación 2: " + str(areas_pis[len(areas_pis)-1]))

#Modificar l’àrea del lavabo i imprimir la nova list area

areas_pis[9] = 10
print("He modificado el area del lavabo: "+ str(areas_pis))
print()

#Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.

patio = 'patio interior'
areas_pis.append(patio)
#Creo una variable asignandole su valor
metros = 2.78
#Con el appened introduzco el valor de la variable en el array
areas_pis.append(metros)

print("He agregado el patio interior y sus metros: "+str(areas_pis))
print()

#Imprimir el total de l’àrea del pis.
print(len(areas_pis))

