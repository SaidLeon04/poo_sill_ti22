"""
    alumno.py
    Nombre: Said Isaac León Lara
    Fecha: 13/02/2023
    Descripción: crear clase alumno para crear objetos con sus atributos
"""
class Alumno:
    __nombre = None
    __matricula = None
    __carrera = None
    def __init__(self):
        print("Alumno")
    def setNombre(self,nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre
    def setMatricula(self,matricula):
        self.__matricula = matricula
    def getMatricula(self):
        return self.__matricula
    def setCarrera(self,carrera):
        self.__carrera = carrera
    def getCarrera(self):
        return self.__carrera

zahid = Alumno()

zahid.setNombre("Zahid") 
print (zahid.getNombre())

zahid.setMatricula("1722110300") 
print (zahid.getMatricula())


zahid.setCarrera("Desarrollo de Software") 
print (zahid.getCarrera())
