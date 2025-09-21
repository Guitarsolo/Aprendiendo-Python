from typing import Optional

def find_employee(employee_ids: list[int], target_id: int) -> Optional[int]:
    """Busca un empleado por su ID en una lista de IDs de empleados.

    Args:
        employee_ids (list[int]): Lista de IDs de empleados.
        target_id (int): ID del empleado a buscar.

    Returns:
        Optional[int]: El ID del empleado si se encuentra, None si no se encuentra.
    """
    if target_id in employee_ids:
        return target_id
    return None


# Ejemplo de uso
employees = [101, 102, 103, 104]
print(find_employee(employees, 102))  # Output: 102
print(find_employee(employees, 999))  # Output: None

