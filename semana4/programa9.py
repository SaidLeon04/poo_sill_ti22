"""
    programa9.py
    Nombre: Said Isaac León Lara
    Fecha: 07/03/2023
    Descripción: Usar un metodo para comprar dos números e imprimir el mayor
"""

def mayor(numero1, numero2): # declaración del método y parametros
	if numero1 > numero2: # primera comparación 
		print(numero1) 
	elif numero2 > numero1: # segunda comparación
		print(numero2)
	else: # en caso de que ninguna comparación se cumpla
		print("Iguales")

mayor (2,3) # argurmentos para el método
mayor (3,2) # argurmentos para el método
mayor (3,3) # argurmentos para el método