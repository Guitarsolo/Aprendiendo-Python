# Crear un iterador para los numeros impares

#limite
limit = 16

# crear el iterador
odd_iter = iter(range(1,limit + 1 ,2)) #range(start, stop, step) step vale 2 para ir consiguiendo los impares

# usar el iterador
for num in odd_iter:
    print(num)

#for num in range(1,limit,2): # aqui el resultado es el mismo, iter es mas eficiente
   # print(num)

