a = [1,2,3,4,5]
b = a
print(a)
print(b)
del a[0]
print(a)
print(b) # se observa que b tambien fue modificado, ya que apunta al mismo espacio de memoria
print(id(a)) # para saber el espacio de memoria
print(id(b))

# Para no apuntar al mismo espacio de memoria, debo usar el slicing
c = a[:]
print(a)
print(c)
print(id(a))
print(id(c))
a.append(6) # modificamos a 
print(a)
print(b)
print(c) # la variable c no se modifica
