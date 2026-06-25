#Clase que representa un producto del restaurante
class Producto:

    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    
    def mostrar_informacion(self):
        return f"{self.nombre} - ${self.precio: .2f} ({self.categoria})"
    
    def __str__(self):
        return self.mostrar_informacion()