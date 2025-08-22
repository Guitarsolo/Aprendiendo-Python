numbers = {1:'Uno',2:'Dos',3:'Tres'}
print(numbers)
print(numbers[2])

information = {'nombre': 'Mariano',
               'apellido':'Díaz',
               'altura':1.86,
               'edad':36}
print(information)
print(information['altura'])
del(information['edad'])
print(information)

claves = information.keys()
print(claves)
print(type(claves))

values = information.values()
print(values)
print(type(values))

pairs = information.items()
print(pairs) # observamos que genera una tupla por cada item

contacts = { 'Mariano':{'apellido':'Díaz',# un diccionario con diccionarios
               'altura':1.86,
               'edad':36},
               'Diego':{'apellido':'Frias',
               'altura':1.77,
               'edad':39}}
print(contacts)
print(contacts['Mariano'])

# Configuración de una aplicación
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}
print("Configuración:", config)

# Contador de palabras
palabras = ["manzana", "banana", "naranja", "manzana", "banana"]
contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print("Contador de palabras:", contador)

# Mapeo de usuarios a datos
usuarios = {
    "user123": {"nombre": "Juan", "edad": 30},
    "user456": {"nombre": "Ana", "edad": 25}
}
print("Datos de usuario user123:", usuarios["user123"])

# Almacenamiento de datos estructurados
libro = {
    "título": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "año": 1967
}
print("Datos del libro:", libro)

# Datos en formato JSON
import json
json_data = json.dumps(libro)
print("Datos en JSON:", json_data)