from abc import ABC, abstractmethod
from ..db.db_conexion import conexion

class RepositorioBase(ABC):
    
    @property
    @abstractmethod
    def tabla(self) -> str:
        """Cada subclase declara su tabla."""
        ...

    @abstractmethod
    def esquema(self, fila) -> object:
        """Cada subclase convierte un Row de SQLite a su modelo."""
        ...

    def obtener_por_id(self, id:int):
        with conexion() as conn:
            fila = conn.execute(f"SELECT * FROM {self.tabla} WHERE id = ?", (id,)).fetchone()
            return self.esquema(fila) if fila else None
    
    def obtener_todos(self,):
        with conexion() as conn:
            resultados = conn.execute(f"SELECT * FROM {self.tabla}")
            return [self.esquema(elemento) for elemento in resultados]
        
    def borrar(self, id:int):
        with conexion() as conn:
            conn.execute(f"DELETE FROM {self.tabla} WHERE id=?", (id,))

