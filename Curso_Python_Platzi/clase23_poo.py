#Fundamentos de la Programación Orientada a Objetos (POO)
#La Programación Orientada a Objetos es un paradigma de programación que organiza el diseño del software en torno a objetos. Los objetos son 
#instancias de clases, que pueden tener atributos (datos) y métodos (funciones).

#Conceptos Clave
# Clase: Es un molde o plantilla que define los atributos y métodos que tendrán los objetos.
# Objeto: Es una instancia de una clase.
# Atributo: Es una variable que pertenece a una clase o a un objeto.
# Método: Es una función que pertenece a una clase o a un objeto.
# Herencia: Es un mecanismo por el cual una clase puede heredar atributos y métodos de otra clase.
# Encapsulamiento: Es el concepto de ocultar los detalles internos de un objeto y exponer sólo lo necesario.
# Polimorfismo: Es la capacidad de diferentes clases de ser tratadas como instancias de la misma clase a través de una interfaz común.

class Person:
    def __init__(self, name, age): # __init__ es un constructor propio y especial de las clases
        self.name = name
        self.age = age
    
    # declarar funciones en la clase (metodos)
    def greet(self): 
        print('Hola, mi nombre es',self.name , 'y tengo', self.age, 'años.')

# crear instancias de la clase
persona1 = Person('Mariano', 36)
persona2 = Person('Maria', 42)

persona1.greet() # llamando al metodo del objeto
persona2.greet()