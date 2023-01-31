"""
    programa6.py
    Nombre: Said Isaac León Lara
    Fecha: 30/01/2023
    Descripción: Calcular el área y perímetro de un triángulo
"""
# menú de opciones para elegir que hacer
print("Escribe 1 para calcular el área y perímetro de un círculo") 
print("Escribe 2 para calcular el área y perímetro de un cuadrado")
print("Escribe 3 para calcular ambos")
op = int(input()) # lee la opción tomada

if op == 1: # calcula solo el área y perímetro del círculo
  radio = float(input("Escribe el radio del círculo:  \n")) # lee una variable flotante llamada radio 
  area = 3.1416 * (radio**2) # calcula el área 
  perimetro = 2 * 3.1416 * radio # calcula el perímetro
  print("El área del círculo con un radio de ", radio,  "cm es: ", area, "\n") # imprime el área del círculo 
  print("El perímetro del círculo con una radio de ", radio, "cm es: ", perimetro, "\n") # imprime el perímetro del círculo 

if op == 2: # calcula solo el área y perímetro del cuadrado
  lado = float(input("Escribe la medida de un lado (cm): ")) # lee una variable flotante llamada lado
  area = lado * lado # calcula el área 
  perimetro = lado * 4 # calcula el perímetro
  print("El área del cuadrado con un lado de ",lado, "cm, es: ", area, "\n") # imprime el área del cuadrado
  print("El perímetro del cuadrado con un lado de ", lado, "cm, es: ", perimetro, "\n") # imprime el perímetro del cuadrado

if op==3: # calcula solo el área y perímetro de un cuadrado y un círculo
  radio = float(input("Escribe el radio de el radio de el círculo: ")) # lee una variable flotante llamada radio
  area_circulo = 3.1416 * (radio**2)  # calcula el área 
  perimetro_circulo = 2 * 3.1416 * radio  # calcula el perímetro
  print("El área del círculo con un radio de ", radio,  "cm es: ", area_circulo, "\n") # imprime el área del circulo
  print("El perímetro del círculo con una radio de ", radio, "cm es: ", perimetro_circulo, "\n") # imprime el perímetro del círculo


  lado = float(input("Escribe la medida de un lado del cuadrado(cm): ")) # lee una variable flotante llamada lado
  area_cuadrado = lado * lado  # calcula el área 
  perimetro_cuadrado = lado * 4  # calcula el perímetro
  print("El área del cuadrado con un lado de ",lado, "cm, es: ", area_cuadrado, "\n") # imprime el área del cuadrado
  print("El perímetro del cuadrado con un lado de : ", lado, "cm, es ", perimetro_cuadrado, "\n") # imprime el perímetro del cuadrado
  