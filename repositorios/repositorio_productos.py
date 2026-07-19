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
            query = f"INSERT INTO {self.tabla} (nombre, descripcion, cantidad, precio, categoria_id) VALUES (?, ?, ?, ?, ?)"
            params = (
                prod.nombre,
                prod.descripcion,
                prod.cantidad,
                prod.precio,
                prod.categoria_id
            )
        else:
            query = f"UPDATE {self.tabla} SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria_id = ? WHERE id = ?", 
            params = (
                prod.nombre,
                prod.descripcion,
                prod.cantidad,
                prod.precio,
                prod.categoria_id,
                prod.id,
            )

        with conexion() as conn:
            cursor = conn.execute(query, params)
            if prod.id is not None and cursor.rowcount == 0:
                raise ValueError(f"No existe un producto con id={prod.id}")
