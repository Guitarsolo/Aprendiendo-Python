#print('Hola mundo)
#res = '10' + 2
#div = 10 / 0

try: # try ejecuta un bloque de codigo, cada try tiene al menos un except
    divisor = int(input('Ingresa un numero divisor: '))
    result = 100 / divisor
    print(result)
except ZeroDivisionError as e: # captura el error en la variable e
    print('Error, el divisor no puede ser cero.')
    print('Ha ocurrido un error:', e)
except ValueError as e:
    print('Error: debes introducir un numero valido')
    print('Ha ocurrido un error:', e)



