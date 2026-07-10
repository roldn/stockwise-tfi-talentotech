from .repositorio_base import RepositorioBase
from db.db_conexion import conexion
from modelos.producto import Producto

class RepositorioProducto(RepositorioBase):

    @property
    def tabla(self) -> str:
        return "productos"
    
    def _from_row(self, fila: Producto):
        return Producto(
            id = fila["id"],
            nombre = fila["nombre"],
            descripcion = fila["descripcion"],
            cantidad = fila["cantidad"],
            precio = fila["precio"],
            categoria_id = fila["categoria_id"],
        )
    
    def guardar(self, prod: Producto):
        query: str
        params: tuple

        if prod.id is None:
            query = f"INSERT INTO {self.tabla} (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?,)"
            params = (
                prod.nombre,
                prod.descripcion,
                prod.cantidad,
                prod.precio,
                prod.categoria_fk,
                prod.id,
            )
        else:
            query = f"UPDATE {self.tabla} SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ? WHERE id = ?", 
            params = (
                prod.nombre,
                prod.descripcion,
                prod.cantidad,
                prod.precio,
                prod.categoria_fk,
                prod.id,
            )

        with conexion() as conn:
            conn.execute(query, params)
