def cabecera():
	with open("despensa.csv","a") as file:
		file.write(f"{sku},{nombre},{unidad}\n")

def insertarProducto(sku,nombre,unidad):
	with open("despensa.csv","a") as file:
		file.write(f"{sku},{nombre},{unidad}\n")

insertarProducto("1","Producto","pieza")
