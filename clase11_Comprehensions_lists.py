#Hacen el codigo mas eficiente en tiempo de ejecucion y tambien requiere menos lineas de codigo
squares = [x**2 for x in range(1,11)] # en esta estructura, se puede usar el for y el if solamente en una linea de codigo
#print('Cuadrados:',squares)

# Transformar grados celcius a fahrenheit
celcius = [0, 10, 20, 30, 40, 50]
#fahrenheit = [celcius[x-1]*(9/5)+32 for x in range(1,6)]
#otra forma equivalente:
fahrenheit = [temp*(9/5)+32 for temp in celcius]
#print('Temperatura en fahrenheit:',fahrenheit)

#Numeros pares
evens = [x for x in range(1,21) if x%2 == 0] # la notacion dice que si tenemos el if y el for, vamos primero con el for
#print(evens)

#Numeros impares
evens = [x for x in range(1,21) if x%2 != 0] # la notacion dice que si tenemos el if y el for, vamos primero con el for
#print(evens)

#hallar la transpuesta de una matriz
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)

#LUEGO DE VER LA ESTRUCTURA FOR E IF, HACER LOS EJERCICIOS PROPUESTOS EN ESTA CLASE