"""
    programa5.py
    Nombre: Said Isaac León Lara
    Fecha: 30/01/2023
    Descripción: calcular el area y perimetro de cualquier triangulo (sin usar if)
"""

base = float(input("Escribe la medida de la base(cm): ")) # lee la base del triangulo
lado1 = float(input("Escribe la medida de un lado(cm): ")) # lee un lado del triangulo
lado2 = float(input("Escribe la medida de un lado(cm): ")) # lee un lado del triangulo
altura = float(input("Escribe la altura de el triangulo(cm): ")) # lee la base del triangulo

perimetro = base + lado1 + lado2 # calcula el perímetro del triangulo
print("El perimetro de tu triangulo es: ", perimetro) # imprime el perímetro del triángulo
area = (base * altura)/2 # calcula el área del triangulo
print("El área de tu triángulo es: ", area) # imprime el área del triangulo
