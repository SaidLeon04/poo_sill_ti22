"""
    programa8.py
    Nombre: Said Isaac León Lara
    Fecha: 07/03/2023
    Descripción: 11 maneras diferentes de comparar 2 números usando if, 
    elif y else, para impirmir el múmero mayor o None en caso de que no haya
"""

def mayor(n1,n2): # declaración de una función llamada mayor que tiene como parametros las variables n1 y n2
    # versión 1 de como comparar dos números e impirmir el mayor
    if n1 > n2: # compara n1 mayor que n2
        print(n1) # imprime n1
    if n2 > n1: # compara n2 mayor que n1
        print(n2) # imprime n2
    if n1 == n2: # compara n1 igual a n2
        print(None) # imprime None 
    
    # versión 2 de como comparar dos números e impirmir el mayor
    if n2 > n1: # compara n2 mayor que n1
        print(n2) # imprime n2
    if n1 > n2: # compara n1 mayor que n2
        print(n1) # imprime n1
    if n1 == n2: # compara n1 igual que n2
        print(None) # imprime None 

    # versión 3 de como comparar dos números e impirmir el mayor
    if n2 < n1: # compara n1 menor que n2
        print(n1) # imprime n1
    elif n2 > n1: # compara n2 mayor que n1
        print(n2) # imprime n2
    else:
        print(None) # imprime None 

    # versión 4 de como comparar dos números e impirmir el mayor
    if n1 < n2: # compara n1 menor que n2
        print(n2) # imprime n2
    elif n2 < n1: # compara n2 menor que n1
        print(n1) # imprime n1
    else:
        print(None) # imprime None 

    # versión 5 de como comparar dos números e impirmir el mayor
    if n2 < n1: # compara n1 menor que n2
        print(n1) # imprime n1
    if n1 < n2: # compara n1 menor que n2
        print(n2) # imprime n2
    if n1 == n2: # compara n1 igual que n2
        print(None) # imprime None 

    # versión 6 de como comparar dos números e impirmir el mayor
    if n1 >= n2: # compara n1 mayor o igual que n2
        if n1 > n2: # compara n1 mayor que n2
            print(n1) # imprime n1
        else:
            print(None) # imprime None 
    else:
        print(n2) # imprime n2

    # versión 7 de como comparar dos números e impirmir el mayor
    if n2 >= n1: # compara n2 mayor o igual que n1
        if n2 > n1: # compara n2 mayor que n1
            print(n2) # imprime n2
        else:
            print(None) # imprime None 
    else:
        print(n1) # imprime n1

    # versión 8 de como comparar dos números e impirmir el mayor
    if n1 <= n2: # compara n1 menor o igual que n2
        if n1 < n2: # compara n1 menor que n2
            print(n2) # imprime n2
        else:
            print(None) # imprime None 
    else:
        print(n1) # imprime n1

    # versión 9 de como comparar dos números e impirmir el mayor
    if n1 <= n2: # compara n1 menor o igual que n2
        if n1 == n2: # compara n1 igual que n2
            print(None) # imprime None 
        else:
            print(n2) # imprime n2
    else:
        print(n1) # imprime n1

    # versión 10 de como comparar dos números e impirmir el mayor
    if n1 == n2: # compara n1 igual que n2
        print(None) # imprime None 
    elif n1 < n2: # compara n1 menor que n2
        print(n2) # imprime n2
    else:
        print(n1) # imprime n1

    # versión 11 de como comparar dos números e impirmir el mayor
    if n1 == n2: # compara n1 igual que n2
        print(None) # imprime None 
    elif n2 > n1: # compara n2 mayor que n1
        print(n2) # imprime n2
    else:
        print(n1) # imprime n1
        
mayor(2,1) # invoca a la función mayor con valor de 2 y 1 para sus parametros
