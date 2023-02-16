"""
    alumno.py
    Nombre: Said Isaac León Lara
    Fecha: 13/02/2023
    Descripción: crear clase alumno para crear objetos con sus atributos
"""
class Alumno: # Crea la clase Alumno
    __nombre = None # declara la variable privada __nombre con valor de None
    __matricula = None # declara la variable privada __matricula con valor de None
    __carrera = None # declara la variable privada __carrera con valor de None
    def __init__(self):# funcion que inicializa la clase
        print("Alumno")# imprime el texto alumno
    def setNombre(self,nombre): # función que asigna un valor a la variable nombre
        self.__nombre = nombre # el valor de __nombre será igual nombre
    def getNombre(self): # función que obtiene el valor de la variable nombre
        return self.__nombre # retorna el valor de __nombre
    
    def setMatricula(self,matricula): # función que asigna un valor a la variable matricula
        self.__matricula = matricula # el valor de __matricula será igual matricula
    def getMatricula(self): # función que obtiene el valor de la variable matricula
        return self.__matricula # retorna el valor de __matricula
    
    def setCarrera(self,carrera): # función que asigna un valor a la variable carrera
        self.__carrera = carrera # el valor de __carrera será igual nombre
    def getCarrera(self): # función que obtiene el valor de la variable carrera
        return self.__carrera # retorna el valor de __carrera

zahid = Alumno() # crea un objeto de la clase Alumno

zahid.setNombre("Zahid") # usa el metodo setNombre para asignar un nombre al objeto
print (zahid.getNombre()) #imprime la funcion getNombre para mostrar el nombre 

zahid.setMatricula("1722110300")  # usa el metodo setMatricula para asignar una matricula al objeto
print (zahid.getMatricula()) #imprime la funcion getNombre para mostrar la matricula 


zahid.setCarrera("Desarrollo de Software")  # usa el metodo setCarrera para asignar una carrera al objeto
print (zahid.getCarrera()) #imprime la funcion getNombre para mostrar la carrera 
