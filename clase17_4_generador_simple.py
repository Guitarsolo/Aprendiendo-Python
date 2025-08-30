def my_generator():
    yield 1
    yield 2
    yield 3

print('recorrer generador con un for:')

for value in my_generator():
    print(value)

# Generador fibonacci
# Fibonacci (secuencia infinita de números naturales que comienza con 1 y 1, y donde cada término siguiente es la suma de los dos anteriores)
# 0 1 1 2 3 5 8 13 21 34

def fibonacci(limit): # el argumento es el limite de la secuencia fibonacci
    a, b = 0, 1 # equivale a decir a = 0 y b = 1
    while a < limit:
        yield a
        a, b = b, a+b # equivale: a = b y b = a + b

for num in fibonacci(50):
    print(num)