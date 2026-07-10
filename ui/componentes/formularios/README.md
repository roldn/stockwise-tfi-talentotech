# formularios

Sub-módulo de la capa `ui`. Contiene los formularios modales de creación y edición de entidades del sistema de inventario.

## Estructura

```
formularios/
├── __init__.py
├── formulario_producto.py
└── formulario_categoria.py
```

## Clases

### `FormularioProducto`

Ventana modal (`tk.Toplevel`) para crear o editar un producto.

```python
from ui.formularios.formulario_producto import FormularioProducto

FormularioProducto(
    parent=self,
    categorias=lista_de_categorias,
    on_guardar=self._manejar_guardado,
    datos=producto_existente  # None para modo creación
)
```

**Parámetros:**

| parámetro   | tipo       | descripción                                                   |
|-------------|------------|---------------------------------------------------------------|
| parent      | tk.Widget  | Ventana padre. El modal queda centrado y bloqueado sobre ella.|
| categorias  | list       | Lista de objetos `Categoria` para poblar el Combobox.         |
| on_guardar  | callable   | Función que recibe un `dict` con los datos validados.         |
| datos       | dict/None  | Si se pasa, el formulario se abre en modo edición precargado. |

**Campos:**

| campo      | tipo   | validación                                      |
|------------|--------|-------------------------------------------------|
| Nombre     | str    | Texto válido según `validar_texto`.             |
| Descripción| str    | Opcional, sin validación.                       |
| Precio     | float  | Solo números, mayor a cero.                     |
| Stock      | int    | Solo enteros, no puede estar vacío.             |
| Categoría  | select | Selección obligatoria desde Combobox.           |

**Dict retornado a `on_guardar`:**
```python
{
    "id": int | None,       # None si es creación
    "nombre": str,
    "descripcion": str,
    "precio": float,
    "cantidad": int,
    "categoria_id": int
}
```

---

### `FormularioCategoria`

Ventana modal (`tk.Toplevel`) para crear o editar una categoría.

```python
from ui.formularios.formulario_categoria import FormularioCategoria

FormularioCategoria(
    parent=self,
    on_guardar=self._manejar_guardado,
    datos=categoria_existente  # None para modo creación
)
```

**Parámetros:**

| parámetro  | tipo      | descripción                                                   |
|------------|-----------|---------------------------------------------------------------|
| parent     | tk.Widget | Ventana padre. El modal queda centrado y bloqueado sobre ella.|
| on_guardar | callable  | Función que recibe un `dict` con los datos validados.         |
| datos      | dict/None | Si se pasa, el formulario se abre en modo edición precargado. |

**Campos:**

| campo       | tipo | validación                          |
|-------------|------|-------------------------------------|
| Nombre      | str  | Texto válido según `validar_texto`. |
| Descripción | str  | Opcional, sin validación.           |

**Dict retornado a `on_guardar`:**
```python
{
    "id": int | None,       # None si es creación
    "nombre": str,
    "descripcion": str
}
```

## Notas

- Ambos formularios bloquean la ventana padre con `grab_set()` mientras están abiertos.
- Los errores de validación se muestran inline debajo de cada campo, sin interrumpir el flujo con popups.
- El modo creación o edición se determina automáticamente según si `datos` es `None` o no.
- La validación es delegada al sub-módulo `servicios/validaciones/`.
