def outer():
    x = 'Outer'  # Variable local a la funcion outer

    # Funcion interna
    def inner():
        nonlocal x  # te permite modificar variables de la función externa (la que "envuelve" a la interna), pero sin llegar a ser una variable global.
        x = 'Inner'  # Modificar la variable no local
        print(f"Valor de x en la funcion inner: {x}")

    inner()
    print(f"Valor de x en la funcion outer: {x}")


outer()
