"""
    programa3.py
    Nombre: Said Isaac León Lara
    Fecha: 24/01/2023
    Descripción: Operaciones aritmeticas dentro de print() y con str.format
"""
variable1 = 10  #  variable para almacenar un entero
variable2 = 5  #  variable para almacenar un entero
print(variable1 + variable2)  #  suma de dos variables
print("{} + {} = {}" .format(variable1, variable2 , variable1+variable2))  #  formatear las variables cambiando su tipo a string, hace la suma e imprime la operación completa
print("{} - {} = {}" .format(variable1, variable2 , variable1-variable2)) # resta muestra la operación completa
print("{} = {} * {}" .format(variable1*variable2, variable1, variable2)) # multiplicación que muestra la operación completa
print("El resultado de dividir {} / {} es {}" .format(variable1, variable2, variable1/variable2)) # división que meustra una cadena para describir la operación