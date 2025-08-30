# Concesionaria de vehiculos en la cual se va a poder hacer la compra y la venta. Ademas de gestionar los vehiculos, un usuario va a poder preguntar
# cuales son los que estan disponibles, su precio, y tambien va a poder comprar uno.

class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = True
    
    def vender(self):
        if self.disponible:
            print(f'El vehiculo {self.marca} {self.modelo} se ha vendido con éxito a {self.precio} pesos.')
            self.disponible = False

        else:
            print(f'El vehiculo {self.marca} {self.modelo} no esta disponible para la venta.')

    def chequear_disponibilidad(self):
        return self.disponible
    
    def obtener_precio(self):
        return self.precio
        
    def hacer_disponible(self):
        self.disponible = True
        print(f'El vehiculo {self.modelo} ahora está disponible para la venta.')

class Cliente:
    def __init__(self, nombre, id_cliente):
        self.nombre = nombre
        self.id_cliente = id_cliente
        self.vehiculos_comprados = []
    
    def comprar_vehiculo(self, vehiculo):
        if vehiculo.chequear_disponibilidad():
            vehiculo.vender()
            self.vehiculos_comprados.append(vehiculo)
            concesionario.quitar_vehiculo(vehiculo)
            print(f'El vehiculo {vehiculo.modelo} ha sido comprado por {self.nombre}.')
        else:
            print(f'El vehiculo {vehiculo.modelo} no esta disponible para la venta.')

    def consultar_vehiculo(self, vehiculo):
        disponibilidad = 'sí' if vehiculo.chequear_disponibilidad() else 'no'
        print(f'El vehiculo {vehiculo.marca} {vehiculo.modelo} {disponibilidad} está disponible y cuesta ${vehiculo.precio}')

    def devolver_vehiculo(self, vehiculo):
        if vehiculo in self.vehiculos_comprados:
            vehiculo.hacer_disponible()
            self.vehiculos_comprados.remove(vehiculo)
            concesionario.agregar_vehiculo(vehiculo)
            print(f'El cliente {self.nombre} ha devuelto el vehiculo {vehiculo.modelo}.')
        else:
            print(f"El vehículo {vehiculo.modelo} no está en la lista de comprados.")

class Concesionario:
    def __init__(self):
        self.inventario = []
        self.clientes = []

    def agregar_vehiculo(self, vehiculo):
        self.inventario.append(vehiculo)
        print(f"El vehículo {vehiculo.marca} {vehiculo.modelo} ha sido agregado al inventario.")

    def quitar_vehiculo(self, vehiculo):
        self.inventario.remove(vehiculo)
        print(f"El vehículo {vehiculo.marca} {vehiculo.modelo} ha sido quitado del inventario.")

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"El cliente {cliente.nombre} ha sido registrado en la concesionaria.")

    def mostrar_vehiculos_disponibles(self):
        print("Vehículos disponibles en la concesionaria:")
        for vehiculo in self.inventario:
            if vehiculo.chequear_disponibilidad():
                print(f"- {vehiculo.marca} {vehiculo.modelo} por ${vehiculo.precio}")

# Crear los vehículos
vehiculo1 = Vehiculo("Honda",'Civic', 38000)
vehiculo2 = Vehiculo("Ford",'Mustang', 62000)
vehiculo3 = Vehiculo('Toyota', 'Corolla', 29000)

# Crear cliente
cliente1 = Cliente("Mariano", "001")

# Crear instancia de concesionario y registrar coches y clientes
concesionario = Concesionario()
concesionario.agregar_vehiculo(vehiculo1)
concesionario.agregar_vehiculo(vehiculo2)
concesionario.agregar_vehiculo(vehiculo3)
concesionario.registrar_cliente(cliente1)

# Mostrar vehículos disponibles
concesionario.mostrar_vehiculos_disponibles()

# Consultar vehiculo
cliente1.consultar_vehiculo(vehiculo3)

# Realizar compra
cliente1.comprar_vehiculo(vehiculo3)

# Mostrar vehículos disponibles
concesionario.mostrar_vehiculos_disponibles()

# Cliente intenta comprar un vehilo ya vendido
cliente1.comprar_vehiculo(vehiculo3)

# Devolver vehículo
cliente1.devolver_vehiculo(vehiculo3)

# Mostrar vehículos disponibles
concesionario.mostrar_vehiculos_disponibles()
