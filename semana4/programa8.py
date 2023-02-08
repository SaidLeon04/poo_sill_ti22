"""
    programa8.py
    Nombre: Said Isaac León Lara
    Fecha: 07/03/2023
    Descripción: 11 maneras diferentes de comparar 2 números usando if, elif y else.
"""

def mayor(n1,n2):
    # v1
    if n1 > n2:
        print(n1)
    if n2 > n1:
        print(n2)
    if n1 == n2:
        print(None)
    
    # v2
    if n2 > n1:
        print(n2)
    if n1 > n2:
        print(n1)
    if n1 == n2:
        print(None)

    # v3
    if n1 < n2:
        print(n1)
    elif n2 > n1:
        print(n2)
    else:
        print(None)

    # v4
    if n1 < n2:
        print(n2)
    elif n2 < n1:
        print(n1)
    else:
        print(None)

    # v5
    if n2 < n1:
        print(n1)
    if n1 < n2:
        print(n2)
    if n1 == n2:
        print(None)

    # v6
    if n1 >= n2:
        if n1 > n2:
            print(n1)
        else:
            print(None)
    else:
        print(n2)

    # v7
    if n2 >= n1:
        if n2 > n1:
            print(n2)
        else:
            print(None)
    else:
        print(n1)

    # v8
    if n1 <= n2:
        if n1 < n2:
            print(n2)
        else:
            print(None)
    else:
        print(n1)    

    # v9
    if n1 <= n2:
        if n1 == n2:
            print(None)
        else:
            print(n2)
    else:
        print(n1)

    # v10
    if n1 == n2:
        print(None)
    elif n1 < n2:
        print(n2)
    else:
        print(n1)

    # v11
    if n1 == n2:
        print(None)
    elif n2 > n1:
        print(n2)
    else:
        print(n1)
mayor(2,1)