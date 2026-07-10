# componentes

Sub-módulo de la capa `ui`. Contiene los componentes reutilizables de la interfaz gráfica del sistema de inventario.

## Estructura

```
componentes/
├── __init__.py
├── tabla.py
└── formularios/
    ├── __init__.py
    ├── formulario_producto.py
    └── formulario_categoria.py
```

## Clases

### `Tabla`

Widget reutilizable basado en `ttk.Treeview`. Encapsula la tabla de datos junto con su barra de acciones y puede usarse para cualquier entidad del sistema.

```python
from ui.componentes.tabla import Tabla

tabla = Tabla(
    parent=self,
    columnas=["ID", "Nombre", "Precio", "Stock", "Categoría"],
    on_nuevo=self._nuevo_producto,
    on_editar=self._editar_producto,
    on_borrar=self._borrar_productos,
)
tabla.pack(fill="both", expand=True)

# Cargar datos
tabla.cargar([
    (1, "Monitor 24\"", 299.99, 10, "Electrónica"),
    (2, "Teclado inalámbrico", 45.00, 15, "Electrónica"),
])
```

**Parámetros del constructor:**

| parámetro  | tipo       | descripción                                                        |
|------------|------------|--------------------------------------------------------------------|
| parent     | tk.Widget  | Contenedor padre del componente.                                   |
| columnas   | list[str]  | Nombres de las columnas a mostrar.                                 |
| on_nuevo   | callable   | Función invocada al presionar "Nuevo".                             |
| on_editar  | callable   | Función invocada al presionar "Editar". Recibe la fila como tuple. |
| on_borrar  | callable   | Función invocada al presionar "Borrar". Recibe lista de tuples.    |

**Métodos públicos:**

| método                      | descripción                                                        |
|-----------------------------|--------------------------------------------------------------------|
| `cargar(filas)`             | Limpia la tabla y carga una lista de tuples como filas.            |
| `obtener_fila_seleccionada()` | Retorna los valores de la fila seleccionada o `None`.            |

**Comportamiento:**

- Los botones "Editar" y "Borrar" permanecen deshabilitados hasta que el usuario selecciona una fila.
- Soporta selección múltiple para borrado en lote, con diálogo de confirmación.
- Si no hay filas, muestra una fila con el texto "Sin registros" en gris.
- Cada columna es clickeable para ordenar de forma ascendente o descendente.

---

### Formularios

Los formularios modales se encuentran en el sub-módulo `formularios/`. Ver [formularios/README.md](formularios/README.md) para la documentación completa.

| clase                | descripción                                      |
|----------------------|--------------------------------------------------|
| `FormularioProducto` | Modal para crear o editar un producto.           |
| `FormularioCategoria`| Modal para crear o editar una categoría.         |
