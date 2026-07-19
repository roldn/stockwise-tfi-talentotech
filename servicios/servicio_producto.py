from repositorios.repositorio_productos import RepositorioProducto
from .servicio_categoria import ServicioCategoria
from .servicio_base import ServicioBase
from modelos.producto import Producto
from .validaciones.validadores_texto import validar_texto
from .validaciones.validadores_numericos import validar_precio


class ServicioProducto(ServicioBase):
    def __init__(self):
        self._repo = RepositorioProducto()
        self._servicio_categoria = ServicioCategoria()

    def obtener_todos(self) -> list[Producto]:
        return self._repo.obtener_todos()
    
    def obtener_por_id(self, id:int) -> Producto:
        producto = self._repo.obtener_por_id(id)
        if producto is None:
            raise ValueError(f"No existe un producto con id = {id}")
        return producto
    
    def guardar(self, datos:dict) -> None:
        self._lanzar_error_si_resultado_es_invalido(validar_texto(datos.get("nombre", ""), "nombre"))
        self._lanzar_error_si_resultado_es_invalido(validar_precio(datos.get("precio", ""), "precio"))

        # valida que la categoria exista antes de guardar
        self._servicio_categoria.obtener_por_id(datos["categoria_id"])

        producto = Producto(
            id=datos.get("id"),
            nombre=datos["nombre"].strip(),
            descripcion=datos.get("descripcion", "").strip(),
            cantidad=datos["cantidad"],
            precio=datos["precio"],
            categoria_id=datos["categoria_id"],
        )
        self._repo.guardar(producto)

    def borrar(self, id: int) -> None:
        if self.obtener_por_id(id):
            self._repo.borrar(id)
