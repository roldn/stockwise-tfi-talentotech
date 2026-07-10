from dataclasses import dataclass

@dataclass
class Categoria:
    nombre: str
    descripcion: str | None = None
    id: int | None = None
