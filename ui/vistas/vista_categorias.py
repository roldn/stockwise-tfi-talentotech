import tkinter as tk
from tkinter import messagebox

from ..componentes.tabla import Tabla
from ..componentes.formularios.formulario_categorias import FormularioCategoria
from servicios.servicio_categoria import ServicioCategoria


class VistaCategorias(tk.Frame):

    def __init__(self, parent, mostrar_vista):
        super().__init__(parent)
        self._mostrar_vista = mostrar_vista
        self._servicio = ServicioCategoria()

        self._construir_ui()
        self.actualizar()

    def _construir_ui(self) -> None:
        self._tabla = Tabla(
            self,
            columnas=["ID", "Nombre", "Descripción"],
            on_nuevo=self._abrir_formulario_nuevo,
            on_editar=self._abrir_formulario_editar,
            on_borrar=self._borrar_categoria,
        )
        self._tabla.pack(fill="both", expand=True, padx=12, pady=12)

    def actualizar(self) -> None:
        categorias = self._servicio.obtener_todos()
        self._tabla.cargar([
            (c.id, c.nombre, c.descripcion)
            for c in categorias
        ])

    def _abrir_formulario_nuevo(self) -> None:
        FormularioCategoria(self, on_guardar=self._guardar_categoria)

    def _abrir_formulario_editar(self, fila: tuple) -> None:
        try:
            categoria = self._servicio.obtener_por_id(int(fila[0]))
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        FormularioCategoria(
            self,
            on_guardar=self._guardar_categoria,
            datos={
                "id": categoria.id,
                "nombre": categoria.nombre,
                "descripcion": categoria.descripcion,
            }
        )

    def _guardar_categoria(self, datos: dict) -> None:
        try:
            self._servicio.guardar(datos)
            self.actualizar()
        except ValueError as e:
            messagebox.showerror("Error al guardar", str(e))

    def _borrar_categoria(self, filas: list) -> None:
        errores = []
        for fila in filas:
            try:
                self._servicio.borrar(int(fila[0]))
            except ValueError as e:
                errores.append(str(e))
        self.actualizar()
        if errores:
            messagebox.showerror("Error al borrar", "\n".join(errores))
