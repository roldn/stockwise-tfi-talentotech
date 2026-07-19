from .repositorio_base import RepositorioBase
from db.db_conexion import conexion
from modelos.categoria import Categoria

class RepositorioCategoria(RepositorioBase):

    @property
    def tabla(self) -> str:
        return "categorias"
    
    def _from_row(self, fila):
        return Categoria(
            id = fila["id"],
            nombre = fila["nombre"],
            descripcion = fila["descripcion"]
        )
    
    def guardar(self, cat: Categoria) -> None:
        query:str
        params:tuple

        if cat.id is None:
            query = f"INSERT INTO {self.tabla} (nombre, descripcion) VALUES (?, ?)"
            params = (cat.nombre, cat.descripcion)  
        else:
            query = f"UPDATE {self.tabla} SET nombre = ?, descripcion = ? WHERE id = ?"
            params = (cat.nombre, cat.descripcion, cat.id,)

        with conexion() as conn:
            conn.execute(query, params)
