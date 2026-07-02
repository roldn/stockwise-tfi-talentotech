from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    descripcion: str
    cantidad: int
    precio: float
    categoria_fk: int
    id: int | None = None 
