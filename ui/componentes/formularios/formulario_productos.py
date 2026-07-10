import tkinter as tk
from tkinter import ttk
from servicios.validaciones.validadores_texto import validar_texto
from servicios.validaciones.validadores_numericos import validar_precio


class FormularioProducto(tk.Toplevel):

    def __init__(self, parent, categorias: list, on_guardar, datos=None):
        super().__init__(parent)
        self.title("Nuevo producto" if datos is None else "Editar producto")
        self.resizable(False, False)
        self._on_guardar = on_guardar
        self._datos = datos or {}
        self._categorias = categorias

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
        self._nombre.pack(fill="x", pady=(2, 12))
        self._err_nombre = tk.Label(frame, text="", foreground="red", font=("", 9), anchor="w")
        self._err_nombre.pack(fill="x", pady=(0, 8))

        tk.Label(frame, text="Descripción", anchor="w").pack(fill="x")
        self._descripcion = tk.Text(frame, height=3, wrap="word")
        self._descripcion.pack(fill="x", pady=(2, 12))

        fila = tk.Frame(frame)
        fila.pack(fill="x", pady=(0, 12))

        col_precio = tk.Frame(fila)
        col_precio.pack(side="left", expand=True, fill="x", padx=(0, 8))
        tk.Label(col_precio, text="Precio *", anchor="w").pack(fill="x")
        self._precio = tk.Entry(col_precio)
        self._precio.insert(0,"0") 
        self._precio.config(validate="key", validatecommand=(self.register(self._solo_numeros), "%P"))
        self._precio.pack(fill="x", pady=(2, 0))
        self._err_precio = tk.Label(col_precio, text="", foreground="red", font=("", 9), anchor="w")
        self._err_precio.pack(fill="x", pady=(0, 8))

        col_cantidad = tk.Frame(fila)
        col_cantidad.pack(side="left", expand=True, fill="x")
        tk.Label(col_cantidad, text="Stock *", anchor="w").pack(fill="x")
        self._cantidad = tk.Entry(col_cantidad)
        self._cantidad.insert(0, "0")
        self._cantidad.config(validate="key", validatecommand=(self.register(self._solo_enteros), "%P"))
        self._cantidad.pack(fill="x", pady=(2, 0))
        self._err_cantidad = tk.Label(col_cantidad, text="", foreground="red", font=("", 9), anchor="w")
        self._err_cantidad.pack(fill="x", pady=(0, 8))

        tk.Label(frame, text="Categoría *", anchor="w").pack(fill="x")
        self._categoria_var = tk.StringVar()
        self._combo = ttk.Combobox(
            frame,
            textvariable=self._categoria_var,
            values=[c.nombre for c in self._categorias],
            state="readonly"
        )
        if self._categorias:
            self._combo.current(0)
        self._combo.pack(fill="x", pady=(2, 16))

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
                
        if "precio" in self._datos:
            self._precio.delete(0, "end")
            self._precio.insert(0, str(self._datos["precio"]))

        if "cantidad" in self._datos:
            self._cantidad.delete(0, "end")
            self._cantidad.insert(0, str(self._datos["cantidad"]))

        if "categoria_id" in self._datos:
            nombres = [c.nombre for c in self._categorias]
            ids = [c.id for c in self._categorias]
            if self._datos["categoria_id"] in ids:
                idx = ids.index(self._datos["categoria_id"])
                self._combo.current(idx)

    def _solo_numeros(self, valor: str) -> bool:
        if valor == "":
            return True
        try:
            float(valor)
            return True
        except ValueError:
            return False

    def _solo_enteros(self, valor: str) -> bool:
        return valor.isdigit() or valor == ""
    
    def _limpiar_errores(self):
        for lbl in (self._err_nombre, self._err_precio, self._err_cantidad):
            lbl.config(text="")

    def _al_guardar(self):
        self._limpiar_errores()
        hay_errores = False
        valores = {}

        validaciones = [
            (self._nombre.get().strip(),   self._err_nombre,   "nombre",   validar_texto,  "texto"),
            (self._precio.get().strip(),   self._err_precio,   "precio",   validar_precio, "numero"),
            (self._cantidad.get().strip(), self._err_cantidad, "cantidad", None,           "entero"),
        ]

        for valor_raw, lbl_error, campo, validador, tipo in validaciones:
            resultado = validador(valor_raw, campo) if validador else None

            match tipo:
                case "texto":
                    if not resultado.valido:
                        lbl_error.config(text=resultado.errores[0])
                        hay_errores = True
                    else:
                        valores[campo] = valor_raw

                case "numero":
                    if not resultado.valido:
                        lbl_error.config(text=resultado.errores[0])
                        hay_errores = True
                    elif float(valor_raw) <= 0:
                        lbl_error.config(text="El precio debe ser mayor a cero.")
                        hay_errores = True
                    else:
                        valores[campo] = float(valor_raw)

                case "entero":
                    if not valor_raw:
                        lbl_error.config(text="El stock no puede estar vacío.")
                        hay_errores = True
                    else:
                        valores[campo] = int(valor_raw)

        if hay_errores:
            return

        categoria = next(
            (c for c in self._categorias if c.nombre == self._categoria_var.get()),
            None
        )

        self._on_guardar({
            "id": self._datos.get("id"),
            "nombre": valores["nombre"],
            "descripcion": self._descripcion.get("1.0", "end-1c").strip(),
            "precio": valores["precio"],
            "cantidad": valores["cantidad"],
            "categoria_id": categoria.id if categoria else None,
        })
        self.destroy()

    def _centrar(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (self.winfo_width() // 2)
        y = (self.winfo_screenheight() // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{x}+{y}")
