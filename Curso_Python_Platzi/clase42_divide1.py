def divide(a : int, b : int) -> float:
    # validar que ambos parametrsos sean enteros
    if not isinstance(a, int) or not isinstance(b, int):    
        raise ValueError("Ambos parámetros deben ser enteros.") # si no son enteros, lanzamos una excepcion ValueError con un mensaje descriptivo. el codigo se detiene aqui y no continua a la siguiente linea. a menos que se maneje la excepcion con un bloque try-except
    # validar que el divisor no sea cero    
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b

# Ejemplo de uso
#print(divide(10, 2))  # Output: 5.0
#print(divide(10, 0))  # Lanza ValueError: El divisor no puede ser cero.
#print(divide(10, '2'))  # Lanza ValueError: Ambos parámetros deben ser enteros.    

try:
    print(divide(10, 2))  # Output: 5.0
    print(divide(10, 0))  # Lanza ValueError: El divisor no puede ser cero.
    #print(divide(10, '2'))  # Lanza ValueError: Ambos parámetros deben ser enteros.    
except ValueError as e:
    print(f"Error: {e}")    

print('el programa continua...')