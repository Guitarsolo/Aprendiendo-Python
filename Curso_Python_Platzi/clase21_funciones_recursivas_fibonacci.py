# serie de fibonacci: 0 1 1 2 3 5 8 13 21...
# F(n)=F(n−1)+F(n−2)
# Con los casos base:
#F(0) = 0
#F(1) = 1

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
number = 8
print(fibonacci(number))

# reto: calcular la sumatoria de numeros naturales
# f(x) = f(x - 1) + f(x - 2)
def sumatoria(n):
    if n == 0:
        return 0
    else:
        return n + sumatoria(n-1)

print(sumatoria(number))