"""
    persona.py
    Nombre: Said Isaac León Lara
    Fecha: 13/02/2023
    Descripción: Crear una clase llamada Persona con dos variable o atributos que obtendran un valor con la función set y lo devolvera con la función get
"""

class Persona: # Crea la clase Persona
    __nombre = None # declara la variable privada __nombre con valor de None
    __email = None # declara la variable privada __email con valor de None
    def __init__(self): # función que inicializa la clase
        print("Persona") # imprime el texto Persona
    def setNombre(self,nombre): # función que asigna un valor a la variable nombre
        self.__nombre = nombre # el valor de __nombre será igual nombre
    def getNombre(self): # función que obtiene el valor de la variable nombre
        return self.__nombre # retorna el valor de __nombre
    def setEmail(self,email): # función que asigna un valor a la variable email
        self.__email = email # el valor de __email será igual email
    def getEmail(self): # función que obtiene el valor de la variable email
        return self.__email # retorna el valor de __email

dejah = Persona() # crea un objeto de la clase Persona

dejah.setNombre("Dejah") # usa el metodo setNombre para asignar un nombre al objeto
print (dejah.getNombre()) #imprime la funcion getNombre para imprimir el nombre 

dejah.setEmail("correo@mascorreo.correo") # usa el metodo setEmail para asignar un email al objeto
print (dejah.getEmail()) # imprime la funcion getEmail para imprimir el email 
