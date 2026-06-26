from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    
    
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.productos = []
        self.clientes = []
        
    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)
        
    def agregar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)
        
        
    def mostrar_informacion(self):
        print(f"\n-----Restaurante: {self.nombre}-----") 
        
        print("\nProductos:")
        for p in self.productos:
            print(p)
            
        print("\nClientes:")
        for c in self.clientes:
            print(c)                