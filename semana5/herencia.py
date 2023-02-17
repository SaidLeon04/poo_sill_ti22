"""
    herencia.py
    Nombre: Said Isaac León Lara
    Fecha: 14/02/2023
    Descripción: Crear una clase persona y una clase alumno que hereda los atributos y metodos de la clase persona
"""

class Persona: # crea la clase Persona
	def __init__(self): # constructor de la clase Persona
		__nombre = None # Crea una variable privada nombre
		print("Persona") # impirme el texto Persona

class Alumno(Persona): # Crea la clase Alumno que hereda de la clase Persona
	def __init__(self): # constructor de la clase Alumno
		super().__init__() # LLama al constructor de la clase Persona
		print("Alumno") # Imprime el texto Alumno

objeto_persona = Persona() # crea un objeto de la clase Persona
objeto_alumno = Alumno() # Crea un objeto de la clase Alumno

objeto_persona.__nombre = "Dejah Thoris" # Asigna un valor en la variable __nombre para el objeto_persona
print(objeto_persona.__nombre) # imprime el valor en __nombre

objeto_alumno.__nombre = "John Carter"  # Asigna un valor en la variable __nombre para el objeto_alumno
print(objeto_alumno.__nombre) # imprime el valor en __nombre
