# implementa una funcion que procese una lista de diccionarios con informacion de empleados, utilizando anotaciones de tipos
# recibira una lista de diccionarios, cada diccionario tendra las claves 'name' (str), 'age' (int) y 'salary' (float)   
# debe devolver una lista de empleados que ganen mas de cierto sueldo.
from typing import List, Dict # importamos List y Dict para las anotaciones de tipos, estas librerias estan en el modulo typing y sirve para definir tipos de datos complejos como listas y diccionarios      
def filter_high_earners(employees: List[Dict[str, object]], threshold: float) -> List[Dict[str, object]]:
    """Filtra empleados que ganan más que un umbral dado.

    Args:
        employees (List[Dict[str, object]]): Lista de diccionarios con información de empleados.
        threshold (float): El umbral de salario para filtrar empleados.

    Returns:
        List[Dict[str, object]]: Lista de empleados que ganan más que el umbral.
    """
    # Usamos una lista por comprensión para filtrar empleados que ganan más que el umbral
    # Verificamos que el salario sea de tipo int o float antes de compararlo con el umbral
    # Una comprehension de listas es una forma concisa de crear listas en Python, su sintaxis es: [expresion for item in iterable if condicion]
    # isinstance es una funcion incorporada en Python que verifica si un objeto es una instancia de una clase o de una tupla de clases, su sintaxis es: isinstance(objeto, tipo)
    high_earners = [emp for emp in employees if isinstance(emp.get('salary'), (int, float)) and emp['salary'] > threshold]
    return high_earners

# Ejemplo de uso
employees_data = [
    {'name': 'Alice', 'age': 30, 'salary': 70000.0},
    {'name': 'Bob', 'age': 24, 'salary': 50000.0},
    {'name': 'Charlie', 'age': 29, 'salary': 120000.0},
    {'name': 'David', 'age': 35, 'salary': 90000.0},
]
threshold_salary = 80000.0
high_earners = filter_high_earners(employees_data, threshold_salary)
print(high_earners)  # Output: [{'name': 'Charlie', 'age':