from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

restaurante = Restaurante("Sabor Costeño")

producto_1 = Producto("Encebollado", 3.50, True)
producto_2 = Producto("Jugo de naranja", 1.25, True)

cliente_1 = Cliente("Daniel Espinoza", 24)
cliente_2 = Cliente("Marta Roldan", 29)

restaurante.agregar_producto(producto_1)
restaurante.agregar_producto(producto_2)

restaurante.agregar_cliente(cliente_1)
restaurante.agregar_cliente(cliente_2)

restaurante.mostrar_informacion()
