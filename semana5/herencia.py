"""
    herencia.py
    Nombre: Said Isaac León Lara
    Fecha: 14/02/2023
    Descripción: Crear una clase persona y una clase alumno que hereda los atributos y metodos de la clase persona
"""

class Persona:
	def __init__(self):
		nombre = None
		print("Persona")

class Alumno(Persona):
	def __init__(self):
		super().__init__() # forma de crear herencia
		print("Alumno")

objeto_persona = Persona()
objeto_alumno = Alumno()

objeto_persona.__nombre = "Dejah Thoris"
print(objeto_persona.__nombre)

objeto_alumno.__nombre = "John Carter"
print(objeto_alumno.__nombre)

objeto_alumno.email = "john@correo.correo"
print(objeto_alumno.email)
