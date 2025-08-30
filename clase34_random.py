import random

#Generar un numero entero aleatorio
randomNumber = random.randint(1, 10)
print(randomNumber)

#Elegir colores aleatorios
colors = ['Rojo', 'Azul', 'Verde']
randomColor = random.choice(colors)
print(randomColor)

#barajar una lista de cartas
cards = ['As', 'Rey', 'Reina', 'Jota', '10']
random.shuffle(cards)
print(cards)
