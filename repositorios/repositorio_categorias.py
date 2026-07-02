from .repositorio_base import RepositorioBase
from ..db.db_conexion import conexion
from ..modelos.categoria import Categoria

class RepositorioCategoria(RepositorioBase):

    @property
    def tabla(self) -> str:
        return "categorias"
    
    def esquema(self, fila):
        return Categoria(
            id = fila["id"],
            categoria = fila["categoria"]
        )
    
    def guardar(self, cat: Categoria) -> None:
        query:str
        params:tuple

        if cat.id is None:
            query = f"INSERT INTO {self.tabla} (categoria) VALUES (?)"
            params = (cat.categoria,)  
        else:
            query = f"UPDATE {self.tabla} SET categoria = ? WHERE id = ?"
            params = (cat.categoria, cat.id,)

        with conexion() as conn:
            conn.execute(query, params)