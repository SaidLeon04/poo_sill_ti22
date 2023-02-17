"""
    persona.py
    Nombre: Said Isaac León Lara
    Fecha: 14/02/2023
    Descripción: Crear una clase llamada Persona que se convertira en la clase padre de
    la clase Alumno, Profesor y Coordinador
"""

class Persona: # crea la clase Persona
    def __init__(self) -> None: # Constructor de la clase Persona
        print("Persona") # Imprime el texto Persona


class Alumno(Persona): # Crea la clase Alumno que hereda de la clase Persona
    def __init__(self) -> None: # Constructor de la clase Alumno
        super().__init__() # Llama al contructor de la clase Persona 
        print("Alumno") # Imprime el texto Alumno

objeto_alumno = Alumno()  # Crea un objeto de la clase Alumno

class Profesor(Persona): # Crea la clase Profesor que hereda de la clase Persona
    def __init__(self) -> None: # Constructor de la clase Profesor
        super().__init__() # Llama al constructor de la clase Persona
        print("Profesor") # Imprime el texto Profesor

objeto_profesor = Profesor() # Crea un objeto de la clase Profesor

class Coordinador(Persona): # Crea la clase Coordinador que hereda de la clase Persona
    def __init__(self) -> None: # Constructor de la clase Coordinador
        super().__init__() # Llama al constructor de la clase Persona
        print("Coordinador") # Imprime el texto Coordinador

objeto_profesor = Coordinador() # Crea un objeto de la clase Coordinador




            

            