#Clase que administra los clientes y productos
class Restaurante:
    def __init__ (self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

#Agregar un producto
    def agregar_producto(self, producto):
        self.productos.append(producto)

#Agragar un cliente
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

#Mostrar todos los producttos
    def mostrar_productos(self):
        print("\n - PRODUCTOS DISPONIBLES - ")
        for producto in self.productos:
            print(producto)

#Mostrar todos los clientes
    def mostrar_clientes(self):
        print("\n - CLIENTES REGISTRADOS - ")
        for cliente in self.clientes:
            print(cliente)

    def __str__(self):
        return f"Restaurante:{self.nombre}"