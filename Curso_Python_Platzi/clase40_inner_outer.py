x = 'Global' # Variable global

# Funcion externa
def outer():
    x = 'Outer' # Variable local a la funcion outer

    # Funcion interna
    def inner():
        x = 'Inner' # Variable local a la funcion inner
        print(f"Valor de x en la funcion inner: {x}")

    inner()
    print(f"Valor de x en la funcion outer: {x}")

outer()
print(f"Valor de x fuera de las funciones: {x}")
# print(f"El valor de la variable local 'y' fuera de la funcion es: {y}") # Esto generaria un error porque y no es accesible fuera de la funcion
