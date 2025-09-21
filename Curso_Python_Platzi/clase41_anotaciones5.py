from typing import Union

def process_salary(salary: Union[int, float]) -> float:
    """Procesa el salario y devuelve el salario con un aumento del 10%.

    Args:
        salary (Union[int, float]): El salario actual, puede ser un entero o un flotante.

    Returns:
        float: El salario con el aumento aplicado.
    """
    if isinstance(salary, int):  # Convertir a float si es int, isinstance es más seguro que type, porque maneja herencia,  su sintaxis es: isinstance(objeto, tipo)   
        salary = float(salary)
    return salary * 1.10    # Aumento del 10%

# Ejemplo de uso
print(process_salary(50000))    # Output: 55000.0
print(process_salary(75000.50))  # Output: 82500.55 