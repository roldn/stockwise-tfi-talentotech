# vistas

Sub-módulo de la capa `ui`. Contiene las vistas principales del sistema de inventario, cada una representando una sección de la aplicación.

## Estructura

```
vistas/
├── __init__.py
├── vista_categorias.py
└── vista_productos.py
```

## Clases

### `VistaCategorias`

Frame principal para la gestión de categorías. Integra el componente `Tabla` con `ServicioCategoria`.

```python
from ui.vistas.vista_categorias import VistaCategorias

vista = VistaCategorias(parent=self, mostrar_vista=self._navegar)
vista.pack(fill="both", expand=True)
```

**Parámetros:**

| parámetro    | tipo      | descripción                                      |
|--------------|-----------|--------------------------------------------------|
| parent       | tk.Widget | Contenedor padre de la vista.                    |
| mostrar_vista| callable  | Función de navegación entre vistas.              |

**Métodos públicos:**

| método       | descripción                                          |
|--------------|------------------------------------------------------|
| `actualizar()` | Recarga los datos desde el servicio y refresca la tabla. |

**Flujo:**

- "Nuevo" abre `FormularioCategoria` en modo creación.
- "Editar" busca la categoría por ID y abre `FormularioCategoria` en modo edición precargado.
- "Borrar" elimina una o más categorías seleccionadas con confirmación previa.
- Los errores de servicio se muestran via `messagebox.showerror`.

---

### `VistaProductos`

Frame principal para la gestión de productos. Integra el componente `Tabla` con `ServicioProducto` y `ServicioCategoria`.

```python
from ui.vistas.vista_productos import VistaProductos

vista = VistaProductos(parent=self, mostrar_vista=self._navegar)
vista.pack(fill="both", expand=True)
```

**Parámetros:**

| parámetro    | tipo      | descripción                                      |
|--------------|-----------|--------------------------------------------------|
| parent       | tk.Widget | Contenedor padre de la vista.                    |
| mostrar_vista| callable  | Función de navegación entre vistas.              |

**Métodos públicos:**

| método         | descripción                                          |
|----------------|------------------------------------------------------|
| `actualizar()` | Recarga los datos desde el servicio y refresca la tabla. |

**Flujo:**

- Incluye una barra de búsqueda en tiempo real que filtra por nombre de producto o nombre de categoría.
- "Nuevo" verifica que existan categorías antes de abrir `FormularioProducto`. Si no hay ninguna, muestra un aviso.
- "Editar" busca el producto por ID y abre `FormularioProducto` en modo edición precargado.
- "Borrar" elimina uno o más productos seleccionados con confirmación previa.
- Los errores de servicio se muestran via `messagebox.showerror`.

## Notas

- Ambas vistas llaman a `actualizar()` automáticamente al inicializarse y después de cada operación de escritura.
- Las categorías se resuelven a nombre legible en `VistaProductos` mediante un diccionario `{id: nombre}` construido desde `ServicioCategoria`.
