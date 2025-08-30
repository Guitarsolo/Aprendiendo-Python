#las funciones lambda y la programacion funcional permiten escribir código más conciso, flexible y expresivo. Vamos a explorarlos en detalle.
# es una función anónima, es decir, una función que no tiene nombre y se define en una sola línea usando la palabra clave lambda. Estas funciones son útiles para operaciones simples y cortas que se pueden definir rápidamente sin la necesidad de una función formal.
# SOLAMENTE NECESITA PARAMETROS Y UNA OPERACION

add = lambda a, b: a + b
print(add(3, 7))

#ejemplo de una definicion de funcion clasica
#def suma(a, b):
 #   return a + b
#print(suma(3, 7))

multiply = lambda a, b: a * b
print(multiply(4, 9))

# si trabajamos con listas y queremos agregar funciones a cada elemento, podemos usar Map acompañado de lambda
# cuadrado de cada numero del cero al 10
numbers = range(11) # hasta el 10
squared_numbers = list(map(lambda x: x**2, numbers))# la función map() aplica una función a cada elemento de un iterable, como una lista o un diccionario. El resultado es un objeto map que se puede convertir a una lista o tupla. 
print(squared_numbers)

# funcion filters permite procesar secuencias (iterables) y extraer los elementos que cumplen con una condición determinada
# numeros pares
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print('Numeros pares:', even_numbers)




