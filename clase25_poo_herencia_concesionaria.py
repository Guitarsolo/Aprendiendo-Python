class Vehiculo: # Superclase
    def __init__(self, marca, modelo, precio):
        # Encapsulación
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = True
    
    def vender(self):
        if self.disponible:
            print(f'El vehículo {self.marca} {self.modelo}. Ha sido vendido.')
            self.disponible = False
        else:
            print(f'El vehículo {self.marca} {self.modelo}. No está disponible.')

    #Abstracción
    def chequear_disponibilidad(self):
        return self.disponible
    
    def obtener_precio(self):
        return self.precio
    
    def encender_motor(self):
        raise NotImplementedError('Este método debe ser implementado por la subclase.')

    def detener_motor(self):
        raise NotImplementedError('Este método debe ser implementado por la subclase.')
          
          
# Herencia
class Auto(Vehiculo):
        # Polimorfismo
        def encender_motor(self):
            if not self.disponible:
                return f'El motor del auto {self.modelo} está en marcha.'
            else:
                return f'{self.modelo} no está disponible.'
            
        def detener_motor(self):
            if self.disponible:
                return f'El motor del auto {self.modelo} se ha detenido.'
            else:
                return f'{self.modelo} no está disponible.' 
            
class Bicicleta(Vehiculo):
        def encender_motor(self):
            if not self.disponible:
                return f'La bicicleta {self.modelo} está en marcha.'
            else:
                return f'{self.modelo} no está disponible.'
            
        def detener_motor(self):
            if self.disponible:
                return f'La bicicleta {self.modelo} se ha detenido.'
            else:
                return f'{self.modelo} no está disponible.' 

class Camion(Vehiculo):
        def encender_motor(self):
            if not self.disponible:
                return f'El motor del camión {self.modelo} está en marcha.'
            else:
                return f'{self.modelo} no está disponible.'
            
        def detener_motor(self):
            if self.disponible:
                return f'El motor del camión {self.modelo} se ha detenido.'
            else:
                return f'{self.modelo} no está disponible.'        

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculos_comprados = []

    def comprar_vehiculo(self, vehiculo : Vehiculo):
        if vehiculo.chequear_disponibilidad():
            vehiculo.vender()
            self.vehiculos_comprados.append(vehiculo)
        else:
            print(f'Lo sentimos, {self.marca} {self.modelo} no está disponible.')

    def consultar_vehiculo(self, vehiculo: Vehiculo):
        if vehiculo.chequear_disponibilidad():
            disponibilidad = 'disponible'
        else:
            disponibilidad = 'no disponible'
        print(f'{vehiculo.marca} {vehiculo.modelo} {disponibilidad} y su precio es ${vehiculo.precio}')

class Concesionaria:
    def __init__(self):
        self.inventario = []
        self.clientes = []
    
    def agregar_vehiculo(self, vehiculo : Vehiculo):
        self.inventario.append(vehiculo)
        print(f'El vehiculo {vehiculo.marca} {vehiculo.modelo} ha sido agregado al inventario.')
    
    def registrar_cliente(self, cliente : Cliente):
        self.cliente.append(cliente)
        print(f'El cliente {cliente.nombre} ha sido registrado.')
    
    def mostrar_vehiculos_disponibles(self):
        print(f'Vehiculos disponibles en el concesionario:')
        for vehiculo in self.inventario:
            if vehiculo.chequear_disponibilidad():
                print(f'- {vehiculo.marca} {vehiculo.modelo} y su precio es {vehiculo.obtener_precio()}.')

auto1 = Auto('Toyota', 'Corolla', 29000)
bicicleta1 = Bicicleta('Yamaha', 'MT-07', 7000)
camion1 = Camion('Scania', 'Model 1', 80000)

cliente1 = Cliente('Carlos')

concesionaria = Concesionaria()
concesionaria.agregar_vehiculo(auto1)
concesionaria.agregar_vehiculo(bicicleta1)
concesionaria.agregar_vehiculo(camion1)

#Mostrar vehiculos disponibles
concesionaria.mostrar_vehiculos_disponibles()

# Cliente consulta un vehiculo
cliente1.consultar_vehiculo(auto1)

# Cliente comprar un vehiculo
cliente1.comprar_vehiculo(auto1)

# Mostrar vehiculos disponibles
concesionaria.mostrar_vehiculos_disponibles()


       
        
    

                
