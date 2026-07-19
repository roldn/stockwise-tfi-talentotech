import tkinter as tk
from tkinter import messagebox

from ..componentes.tabla import Tabla
from ..componentes.formularios.formulario_productos import FormularioProducto
from servicios.servicio_producto import ServicioProducto
from servicios.servicio_categoria import ServicioCategoria


class VistaProductos(tk.Frame):

    def __init__(self, parent, mostrar_vista):
        super().__init__(parent)
        self._mostrar_vista = mostrar_vista
        self._servicio = ServicioProducto()
        self._servicio_categoria = ServicioCategoria()

        self._construir_ui()
        self.actualizar()

    def _construir_ui(self) -> None:

        # Barra de búsqueda
        barra = tk.Frame(self)
        barra.pack(fill="x", padx=12, pady=(12, 0))

        tk.Label(barra, text="Buscar:").pack(side="left", padx=(0, 6))
        self._var_busqueda = tk.StringVar()
        self._var_busqueda.trace_add("write", lambda *_: self.actualizar())
        tk.Entry(barra, textvariable=self._var_busqueda, width=30).pack(side="left")

        # Filtro por categoría
        tk.Label(barra, text="Categoría:").pack(side="left", padx=(12, 6))
        self._var_categoria = tk.StringVar(value="Todas")
        self._opciones_categoria = ["Todas"]
        self._menu_categoria = tk.OptionMenu(
            barra,
            self._var_categoria,
            *self._opciones_categoria,
            command=lambda _: self.actualizar(),
        )
        self._menu_categoria.pack(side="left")

        # Tabla
        self._tabla = Tabla(
            self,
            columnas=["ID", "Nombre", "Precio", "Stock", "Categoría"],
            on_nuevo=self._abrir_formulario_nuevo,
            on_editar=self._abrir_formulario_editar,
            on_borrar=self._borrar_producto,
        )
        self._tabla.pack(fill="both", expand=True, padx=12, pady=12)

    def actualizar(self) -> None:
        productos = self._servicio.obtener_todos()
        categorias = {c.id: c.nombre for c in self._servicio_categoria.obtener_todos()}

        # Actualizar opciones del dropdown
        opciones = ["Todas"] + sorted(categorias.values())
        menu = self._menu_categoria["menu"]
        menu.delete(0, "end")
        for opcion in opciones:
            menu.add_command(label=opcion, command=lambda o=opcion: (self._var_categoria.set(o), self.actualizar()))
        
        # Filtro por nombre
        busqueda = self._var_busqueda.get().strip().lower()
        if busqueda:
            productos = [p for p in productos if busqueda in p.nombre.lower()]

        self._tabla.cargar([
            (p.id, p.nombre, p.precio, p.cantidad, categorias.get(p.categoria_id, "Sin categoría"))
            for p in productos
        ])

    def _abrir_formulario_nuevo(self) -> None:
        categorias = self._servicio_categoria.obtener_todos()
        if not categorias:
            messagebox.showwarning(
                "Sin categorías",
                "Debés crear al menos una categoría antes de agregar productos."
            )
            return
        FormularioProducto(self, categorias=categorias, on_guardar=self._guardar_producto)

    def _abrir_formulario_editar(self, fila: tuple) -> None:
        categorias = self._servicio_categoria.obtener_todos()
        try:
            producto = self._servicio.obtener_por_id(int(fila[0]))
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        FormularioProducto(
            self,
            categorias=categorias,
            on_guardar=self._guardar_producto,
            datos={
                "id": producto.id,
                "nombre": producto.nombre,
                "descripcion": producto.descripcion,
                "precio": producto.precio,
                "cantidad": producto.cantidad,
                "categoria_id": producto.categoria_id,
            }
        )

    def _guardar_producto(self, datos: dict) -> None:
        try:
            self._servicio.guardar(datos)
            self.actualizar()
        except ValueError as e:
            messagebox.showerror("Error al guardar", str(e))

    def _borrar_producto(self, filas: list) -> None:
        errores = []
        for fila in filas:
            try:
                self._servicio.borrar(int(fila[0]))
            except ValueError as e:
                errores.append(str(e))
        self.actualizar()
        if errores:
            messagebox.showerror("Error al borrar", "\n".join(errores))
