class Producto:
    
    def __init__(self, nombre: str, precio: float, disponible: bool):
        self.nombre = nombre
        self.precio = precio
        self.disponible = disponible
        
    def __str__(self):
        return f"Producto: {self.nombre} | Precio: {self.precio} | Disponible: {self.disponible}"
        