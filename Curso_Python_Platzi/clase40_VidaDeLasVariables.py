# Las variables globales son aquellas que se definen fuera de cualquier funcion y son 
# accesibles desde cualquier parte del codigo

# Las variables locales son aquellas que se definen dentro de una funcion y solo son
# accesibles dentro de esa funcion

# Ejemplo

# Variable global
x = 10

def mi_funcion():
    # Variable local
    y = 5
    print(f"El valor de la variable local 'y' es: {y}")
    print(f"El valor de la variable global 'x' es: {x}")

mi_funcion()
print(f"El valor de la variable global 'x' fuera de la funcion es: {x}")