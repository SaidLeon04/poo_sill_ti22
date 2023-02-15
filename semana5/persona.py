"""
    persona.py
    Nombre: Said Isaac León Lara
    Fecha: 13/02/2023
    Descripción: Crear un objeto llamado persona para usar los metodos get, set e init.
"""

class Persona:
    __nombre = None
    __email = None
    def __init__(self): # función que inicializa la clase
        print("Persona")
    def setNombre(self,nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre
    def setEmail(self,email):
        self.__email = email
    def getEmail(self):
        return self.__email

dejah = Persona() # creación del objeto llamado dejah

dejah.setNombre("Dejah") 
print (dejah.getNombre())

dejah.setEmail("correo@mascorreo.correo") 
print (dejah.getEmail())
