"""
    programa4.py
    Nombre: Said Isaac León Lara
    Fecha: 30/01/2023
    Descripción: calcular el area y perimetro de cualquier triangulo (sin usar if)
"""

base = float(input("Escribe la medida de la base(cm): "))
lado1 = float(input("Escribe la medida de un lado(cm): "))
lado2 = float(input("Escribe la medida de un lado(cm): "))
altura = float(input("Escribe la altura de el triangulo(cm): "))

perimetro = base + lado1 + lado2
print("El perimetro de tu triangulo es: ", perimetro)
area = (base * altura)/2
print("El área de tu triángulo es: ", area)
