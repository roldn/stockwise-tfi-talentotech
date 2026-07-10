import tkinter as tk
from .vistas.vista_productos import VistaProductos
from .vistas.vista_categorias import VistaCategorias

class BarraNavegacion(tk.Frame):

    VISTAS = [
        (VistaProductos, "Productos"),
        (VistaCategorias, "Categorías"),
    ]

    def __init__(self, parent, mostrar_vista):
        super().__init__(parent, bd=1, relief="flat")
        self._mostrar_vista = mostrar_vista
        self._botones: dict = {}

        self._construir_ui()

    # ─── Construcción ────────────────────────────────────────────────

    def _construir_ui(self) -> None:
        tk.Label(
            self,
            text="StockFlow",
            font=("", 11, "bold"),
            padx=12,
        ).pack(side="left")

        separador = tk.Frame(self, width=1, bg="gray80")
        separador.pack(side="left", fill="y", pady=4)

        for vista_clase, etiqueta in self.VISTAS:
            btn = tk.Button(
                self,
                text=etiqueta,
                relief="flat",
                padx=12,
                pady=6,
                cursor="hand2",
                command=lambda v=vista_clase: self._al_clickear(v),
            )
            btn.pack(side="left")
            self._botones[vista_clase] = btn

    # ─── Navegación ──────────────────────────────────────────────────

    def _al_clickear(self, vista_clase) -> None:
        self._actualizar_botones(vista_clase)
        self._mostrar_vista(vista_clase)

    def _actualizar_botones(self, vista_activa) -> None:
        for vista_clase, btn in self._botones.items():
            if vista_clase == vista_activa:
                btn.config(relief="sunken", bg="lightblue")
            else:
                btn.config(relief="flat", bg="SystemButtonFace")
