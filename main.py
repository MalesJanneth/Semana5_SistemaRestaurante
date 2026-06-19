#Importar clases
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

#Crear restaurante
restaurante = Restaurante("\n- Delicias Mercy -")

#Crear producto
producto1 = Producto("Seco de pollo", 6, "segundos")
producto2 = Producto("Caldo de bola", 8, "sopas")
producto3 = Producto("Jugo de mora", 1.50, "bebidas")

#Crear clientes
cliente1 = Cliente("Paulina Males", "0988598307")
cliente2 = Cliente("Mercedes Conejo", "0991470674")

#Registrar productos
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)

 #Registrar clientes
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

#Mostrar información
print(restaurante)

restaurante.mostrar_productos()
restaurante.mostrar_clientes()
