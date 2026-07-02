from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    descripcion: str
    cantidad: int
    precio: float
    categoria: str
    id: int | None = None 
