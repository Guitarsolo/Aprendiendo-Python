class Employee:
    def __init__(self, name: str, age: int, salary: float) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def introduce(self) -> str:
        return f"Hola, mi nombre es {self.name}, tengo {self.age} años y mi salario es ${self.salary:.2f}."
    
employee1 = Employee("Mariano Diaz", 30, 60000.00)

print(employee1.introduce())

