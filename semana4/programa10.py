"""
    programa10.py
    Nombre: Said Isaac León Lara
    Fecha: 07/03/2023
    Descripción: Usar typing el los parametros del método para declarar el tipo de dato que son. Utiliza el método para retornar el número mayor o None
"""
def mayor(numero1:int, numero2:int)->int: # método con typing de tipo int
	mayor = None # variable mayor que comienza con el valor de None
	if numero1 > numero2:
		mayor = numero1 # asignación del valor de numero1 a la variable mayor
	elif numero2 > numero1:
		mayor = numero2 # asignación del valor de numero2 a la variable mayor
	else:
		mayor = None # asignación de None a la variable mayor
	return mayor # retorna el valor que hay en mayor después de las comparaciones

print (mayor(3,2)) # argumentos para el método
print (mayor(2,3)) # argumentos para el método
print (mayor(3,3)) # argumentos para el método