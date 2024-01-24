precio =input("Precio del articulo:")
iva = input("Iva del articulo: ")

iva = int(precio)*(int(iva)/100)

resultado = int(precio)+ iva
print(resultado)
