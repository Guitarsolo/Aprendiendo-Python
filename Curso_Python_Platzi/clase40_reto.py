# --- Variable Global ---
# Este es el sueldo mínimo que un empleado debe tener para ser considerado.
# Al ser global, es accesible desde cualquier función en este script.
MINIMUM_SALARY_THRESHOLD = 50000

def filter_high_salary_employees(employee_list):
    """
    Filtra una lista de empleados para encontrar aquellos que ganan más
    que el sueldo definido en la variable global MINIMUM_SALARY_THRESHOLD.
    """
    # --- Variable Local ---
    # 'high_earners' es una lista que solo existe dentro de esta función.
    # Se crea cada vez que la función es llamada y se destruye cuando termina.
    high_earners = []

    for employee in employee_list:
        # Accedemos a la variable global para comparar
        if employee['salary'] > MINIMUM_SALARY_THRESHOLD:
            high_earners.append(employee)

    return high_earners

def run_employee_analysis():
    """
    Función principal que define los datos y ejecuta el filtro.
    """
    # --- Variable Local ---
    # 'employees' es una lista de diccionarios que solo existe localmente
    # en esta función.
    employees = [
        {'name': 'Alice', 'age': 30, 'salary': 60000},
        {'name': 'Bob', 'age': 45, 'salary': 45000},
        {'name': 'Charlie', 'age': 32, 'salary': 75000},
        {'name': 'David', 'age': 28, 'salary': 48000},
        {'name': 'Eve', 'age': 50, 'salary': 90000},
    ]

    print(f"Empleados que ganan más de ${MINIMUM_SALARY_THRESHOLD}:")
    
    # Llamamos a la función de filtrado
    result = filter_high_salary_employees(employees)
    
    # Imprimimos el resultado
    for employee in result:
        print(f"- {employee['name']} (Salario: ${employee['salary']})")


# --- Punto de entrada del script ---
if __name__ == "__main__":
    run_employee_analysis()
