# Definicion de la funcion
def greet(name, last_name = 'Guerra'): # aqui el parametro last name tiene un valor por defecto
    print('Hola', name, last_name)

# Llamado a la funcion
greet('Mariano','Diaz')
greet('Margarita')
greet(last_name='Diaz', name='Marian') # se obtiene el mismo orden de posicion de la deficinion de la funcion (parametros posicionales)

