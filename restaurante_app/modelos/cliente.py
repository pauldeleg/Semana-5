class Cliente:
    
    
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
        
        
    def __str__(self):
        return f"Cliente:  {self.nombre} | {self.edad}"
        