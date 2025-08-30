def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator():
    while True: # bucle infinito
        print('Seleccione una opción:')
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicación')
        print('4. División')
        print('5. Salir')
        
        option = int(input('Ingrese la opcion solicitada: '))

        if option == 5:
            print('Saliendo de la calculadora')
            break

        if option in [1, 2, 3, 4]:
            num1 = float(input('Ingrese el primer número: '))
            num2 = float(input('Ingrese el segundo número: '))

            if option == 1:
                print('El resultado de la suma es:')
                print(add(num1, num2))
            elif option == 2:
                print('El resultado de la resta es:')
                print(substract(num1, num2))
            elif option == 3:
                print('El resultado de la multiplicación es:')
                print(multiply(num1, num2))
            elif option == 4:
                print('El resultado de la división es:')
                print(divide(num1, num2))
        else:
            print('Opción no valida, por favor intenta de nuevo')
calculator()
    






        

