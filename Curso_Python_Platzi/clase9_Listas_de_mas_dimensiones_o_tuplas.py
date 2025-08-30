matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix)
print(matrix[1][2])# acceder al 6

# Tuplas: son inmutables, no podemos hacer cambios en ellas unas vez establecidas
numbers = (1,2,3,4,5) # se pueden omitir los parentesis y es valido, python lo reconoce como tupla
print(numbers)
print(type(numbers))
print(numbers[3])
# numbers[0] = 'Uno' # esto genera un error, porque es una tupla inmutable
print(numbers)


