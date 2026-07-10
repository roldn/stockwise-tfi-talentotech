import tkinter as tk
from tkinter import ttk, messagebox 

class Tabla(tk.Frame):
    def __init__(self, parent, columnas:list[str], on_nuevo=None, on_editar=None, on_borrar=None):
        super().__init__(parent)

        self._on_editar = on_editar
        self._on_borrar = on_borrar

        self._construir_botones(on_nuevo)
        self._construir_tabla(columnas)
        self._construir_scroll()

    # ─── Construcción ────────────────────────────────────────────────

    def _construir_botones(self, on_nuevo) -> None:
        barra = tk.Frame(self)
        barra.pack(fill="x", pady=(0,4))

        self._btn_nuevo = tk.Button(
            barra,
            text="Nuevo",
            command=on_nuevo,
        )
        self._btn_nuevo.pack(side="left", padx=(0,4))

        self._btn_editar = tk.Button(
            barra,
            text="Editar",
            state="disabled",
            command=self._confirmar_editar,
        )
        self._btn_editar.pack(side="left", padx=(0,4))
        
        self._btn_borrar = tk.Button(
            barra,
            text="Borrar",
            state="disabled",
            command=self._confirmar_borrar,
        )
        self._btn_borrar.pack(side="left")

    def _construir_tabla(self, columnas: list[str]) -> None:
        contenedor = tk.Frame(self)
        contenedor.pack(fill="both", expand=True)

        self._tabla = ttk.Treeview(
            contenedor,
            columns=columnas,
            show="headings",
            selectmode="extended",
        )

        for col in columnas:
            self._tabla.heading(col, text=col, command=lambda c=col: self._ordenar(c, False))
            self._tabla.column(col, minwidth=80, width=140, stretch=True)

        self._tabla.pack(side="left", fill="both", expand=True)
        self._tabla.bind("<<TreeviewSelect>>", self._al_seleccionar)

    def _construir_scroll(self) -> None:
        scroll = ttk.Scrollbar(self, orient="vertical", command= self._tabla.yview)
        self._tabla.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")

    # ─── Datos ───────────────────────────────────────────────────────

    def cargar(self, filas: list[tuple]) -> None:
        """Limpia la tabla y carga nuevas filas."""
        
        self._limpiar()
        
        if not filas:
            self._mostrar_vacio()
            return
        
        for fila in filas:
            self._tabla.insert("", "end", values=fila)
    
    def _limpiar(self) -> None:
        for item in self._tabla.get_children():
            self._tabla.delete(item)
        pass
    
    def _mostrar_vacio(self) -> None:
        """Inserta una fila indicando que no hay datos."""
        cols = len(self._tabla["columns"])
        valores = ("Sin registros",) + ("",) * (cols - 1)
        self._tabla.insert("", "end", values=valores, tags=("vacio",))
        self._tabla.tag_configure("vacio", foreground="gray")

    def obtener_fila_seleccionada(self) -> tuple | None:
        """Devuelve los valores de la fila seleccionada, o None si no hay selección."""
        seleccion = self._tabla.selection()
        if not seleccion:
            return None
        return self._tabla.item(seleccion[0])["values"]
    
    # ─── Eventos ─────────────────────────────────────────────────────

    def _al_seleccionar(self, event) -> None:
        """Habilita o deshabilita los botones de editar y borrar según la selección."""
        fila = self.obtener_fila_seleccionada()
        tiene_seleccion = fila is not None and fila != ("Sin registros",)
        estado = "normal" if tiene_seleccion else "disabled"
        self._btn_editar.config(state=estado)
        self._btn_borrar.config(state=estado)

    def _confirmar_editar(self) -> None:
        fila = self.obtener_fila_seleccionada()
        if fila and self._on_editar:
            self._on_editar(fila)
        
    def _confirmar_borrar(self) -> None:
        seleccion = self._tabla.selection()
        if not seleccion:
            return

        cantidad = len(seleccion)
        mensaje = (
            "¿Seguro que querés borrar este registro?"
            if cantidad == 1
            else f"¿Seguro que querés borrar estos {cantidad} registros?"
        )

        confirmado = messagebox.askyesno(title="Confirmar borrado", message=mensaje)
        if confirmado and self._on_borrar:
            filas = [self._tabla.item(item)["values"] for item in seleccion]
            self._on_borrar(filas)

    def _ordenar(self, columna:str, descendente: bool) -> None:
        """Ordena la tabla por la columna especificada."""
        filas = [
            (self._tabla.set(item, columna), item)
            for item in self._tabla.get_children()
        ]
        filas.sort(reverse=descendente)
        for indice, (valor, item) in enumerate(filas):
            self._tabla.move(item, "", indice)

        self._tabla.heading(
            columna,
            command = lambda: self._ordenar(columna, not descendente)
        )
