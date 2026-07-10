import tkinter as tk
from .barra_navegacion import BarraNavegacion
from .vistas.vista_productos import VistaProductos
from .vistas.vista_categorias import VistaCategorias


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("StockFlow")
        self.geometry("960x600")
        self.minsize(800, 500)

        self._frames: dict = {}

        self._construir_ui()
        self.mostrar_vista(VistaProductos)

    # ─── Construcción ────────────────────────────────────────────────

    def _construir_ui(self) -> None:
        self._navbar = BarraNavegacion(self, self.mostrar_vista)
        self._navbar.pack(side="top", fill="x")

        self._contenedor = tk.Frame(self)
        self._contenedor.pack(fill="both", expand=True)
        self._contenedor.grid_rowconfigure(0, weight=1)
        self._contenedor.grid_columnconfigure(0, weight=1)

        for Vista in (VistaProductos, VistaCategorias):
            frame = Vista(self._contenedor, self.mostrar_vista)
            frame.grid(row=0, column=0, sticky="nsew")
            self._frames[Vista] = frame

    # ─── Navegación ──────────────────────────────────────────────────

    def mostrar_vista(self, vista_clase) -> None:
        frame = self._frames.get(vista_clase)
        if frame:
            frame.actualizar()
            frame.tkraise()
