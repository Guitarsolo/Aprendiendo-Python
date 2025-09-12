def add_id_employee_ids(id1: int, id2: int) -> int:
    """
    Suma dos IDs de empleados y retorna el total.
    
    :param id1: Primer ID de empleado (entero).
    :param id2: Segundo ID de empleado (entero).
    :return: Suma de los dos IDs (entero).
    """
    return id1 + id2


# Mostrar resultado
print(f"Total de IDs: {add_id_employee_ids(100, 101)}")