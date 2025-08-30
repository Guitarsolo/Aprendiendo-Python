# La recursividad es una técnica en la que una función se llama a sí misma para resolver un problema dividiéndolo en subproblemas más pequeños. Es útil cuando un problema puede descomponerse en versiones más simples de sí mismo.

# hayar el factorial de un numero
# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4!
# 4! = 4 * 3!
# factorial(N) = N * factorial(N - 1)

# Caso base: Es la condición que detiene la recursión. Sin un caso base, la función se llamaría indefinidamente y causaría un desbordamiento de pila (stack overflow).
# para el ejemplo del factorial el caso base es N = 0 ya que no se puede calcular y ahi termina la funcion

# funcion recursiva:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial_5 = print(factorial(5))

#
    
