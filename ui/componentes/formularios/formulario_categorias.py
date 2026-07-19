import tkinter as tk
from servicios.validaciones.validadores_texto import validar_texto

class FormularioCategoria(tk.Toplevel):

    def __init__(self, parent, on_guardar, datos=None):
        super().__init__(parent)
        self.title("Nueva categoría" if datos is None else "Editar categoría")
        self.resizable(False, False)
        self._on_guardar = on_guardar
        self._datos = datos or {}

        self._construir_ui()
        self._precargar_datos()

        self.transient(parent)
        self.grab_set()
        self._centrar()

    def _construir_ui(self):
        frame = tk.Frame(self, padx=20, pady=16)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Nombre *", anchor="w").pack(fill="x")
        self._nombre = tk.Entry(frame)
        self._nombre.pack(fill="x", pady=(2, 0))
        self._err_nombre = tk.Label(frame, text="", foreground="red", font=("", 9), anchor="w")
        self._err_nombre.pack(fill="x", pady=(0, 8))

        tk.Label(frame, text="Descripción", anchor="w").pack(fill="x")
        self._descripcion = tk.Text(frame, height=3, wrap="word")
        self._descripcion.pack(fill="x", pady=(2, 16))

        tk.Frame(frame, height=1, bg="gray80").pack(fill="x", pady=(0, 8))

        botones = tk.Frame(frame)
        botones.pack(fill="x")
        tk.Button(botones, text="Cancelar", command=self.destroy).pack(side="right", padx=(4, 0))
        tk.Button(botones, text="Guardar", command=self._al_guardar).pack(side="right")

    def _precargar_datos(self):
        if "nombre" in self._datos:
            self._nombre.insert(0, self._datos["nombre"])
        if "descripcion" in self._datos:
            self._descripcion.insert("1.0", self._datos.get("descripcion", ""))

    def _limpiar_errores(self):
        self._err_nombre.config(text="")

    def _al_guardar(self):
        self._limpiar_errores()
        hay_errores = False
        valores = {}

        resultado = validar_texto(self._nombre.get().strip(), "nombre")
        if not resultado.valido:
            self._err_nombre.config(text=resultado.errores[0])
            hay_errores = True
        else:
            valores["nombre"] = self._nombre.get().strip()

        if hay_errores:
            return

        self._on_guardar({
            "id": self._datos.get("id"),
            "nombre": valores["nombre"],
            "descripcion": self._descripcion.get("1.0", tk.END).rstrip("\n").strip(),
        })
        self.destroy()

    def _centrar(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (self.winfo_width() // 2)
        y = (self.winfo_screenheight() // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{x}+{y}")
