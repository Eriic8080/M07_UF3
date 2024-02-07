#Demanar a l’usuari que introdueixi un valor en €, seguidament demanar que introdueixi el IVA a aplicar-hi 
#(4%, 10% o 21%) i finalment mostrar, per pantalla, 
#el resultat del valor indicat per l’usuari, el % d’IVA demanat per l’usuari i el valor final amb l’IVA afegit.


precio =input("Precio del articulo:")
iva = input("Iva del articulo: ")

iva = int(precio)*(int(iva)/100)

resultado = int(precio)+ iva
print(resultado)
