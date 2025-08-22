numbers = [1,2,3,4,5,6]

for i in numbers:
    print ('Aquí i es igual a:',i)

#Tambien podemos darle el inicio y el final
for i in range(10): # si no se especifica, range siempre comienza de cero
    print('Ejemplo 2:', i)

for i in range(3, 10):
    print('Ejemplo 3:', i)

fruits = ['Manzana','Pera','Uva','Naranja','Tomate']
for fruit in fruits:
    print(fruit)
    if fruit == 'Naranja':
        print ('Naranja encontrada')

# Bucle While
x = 0
while x<5:
    if x == 3:
        break # break sale del bucle, mientras que continue sigue
    print(x)
    
    x += 1

