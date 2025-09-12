x = 5 #Variable global

def modify_global():
    global x  # Declarar que queremos usar la variable global 'x'
    print(f"Valor de x dentro de la funcion antes de modificar: {x}")
    x = 10  # Modificar la variable global
    print(f"Valor de x dentro de la funcion despues de modificar: {x}")

modify_global()
print(f"Valor de x fuera de la funcion: {x}")