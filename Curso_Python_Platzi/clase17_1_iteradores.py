# Ejemplo de iterador
# Los iteradores tienen la ventaja de ocupar menos memoria y de ser procesados con mayor velocidad que una estructura de datos tradicional ya que sus elementos son creados al momento de usarlos y no desde antes como las listas. Para construir un iterador sin pasar por otra estructura, es necesario el uso de clases. Por otro lado Un generador se puede interpretar como sugar syntax de los iteradores.

# Crear lista
my_list = [1,2,3,4]

# Obtener el iterador
my_iter = iter(my_list) # iter() es un objeto que permite recorrer secuencialmente una estructura de datos, como una lista, tupla o diccionario

# Usar el iterador
print(next(my_iter)) # next() devuelve el siguiente valor de un iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

