from repositorios.repositorio_categorias import RepositorioCategoria
from .servicio_base import ServicioBase
from .validaciones.validadores_texto import validar_texto
from modelos.categoria import Categoria

class ServicioCategoria(ServicioBase):
    def __init__(self):
       self._repo = RepositorioCategoria()

    def obtener_todos(self) -> list[Categoria]: 
        return self._repo.obtener_todos()
    
    def obtener_por_id(self, id: int) -> Categoria:
        categoria = self._repo.obtener_por_id(id)
        if categoria is None:
            raise ValueError(f"No existe una categoria con id = {id}")
        return categoria
    
    def guardar(self, datos: dict) -> None:
        self._lanzar_error_si_resultado_es_invalido(
            validar_texto(datos.get("nombre", ""), "nombre")
        )
        categoria = Categoria(
            id=datos.get("id"),
            nombre=datos["nombre"].strip(),
            descripcion=datos.get("descripcion", ""),
        )
        self._repo.guardar(categoria)

    def borrar(self, id:int) -> None:
        if self.obtener_por_id(id):
            self._repo.borrar(id)
