# servicios

Módulo de lógica de negocio del sistema de inventario. Actúa como capa intermedia entre los repositorios y la interfaz de usuario, aplicando validaciones antes de persistir datos.

## Estructura

```
servicios/
├── __init__.py
├── servicio_base.py
├── servicio_categoria.py
├── servicio_producto.py
└── validaciones/
    ├── __init__.py
    ├── resultado_validacion.py
    ├── validadores_texto.py
    └── validadores_numericos.py
```

## Clases

### `ServicioBase`

Clase base que provee el método de validación compartido por todos los servicios.

| método | descripción |
|---|---|
| `_lanzar_error_si_resultado_es_invalido(resultado)` | Lanza `ValueError` si el `ResultadoValidacion` recibido es inválido. |

---

### `ServicioCategoria`

Maneja la lógica de negocio para la entidad `Categoria`.

```python
from servicios.servicio_categoria import ServicioCategoria

servicio = ServicioCategoria()

# Listar todas
categorias = servicio.obtener_todos()

# Buscar por ID (lanza ValueError si no existe)
cat = servicio.obtener_por_id(1)

# Insertar nueva
servicio.guardar({"nombre": "Electrónica"})

# Eliminar
servicio.borrar(1)
```

| método | descripción |
|---|---|
| `obtener_todos()` | Retorna lista de todas las categorías. |
| `obtener_por_id(id)` | Retorna la categoría o lanza `ValueError` si no existe. |
| `guardar(datos)` | Valida el nombre y persiste la categoría. |
| `borrar(id)` | Verifica existencia y elimina la categoría. |

---

### `ServicioProducto`

Maneja la lógica de negocio para la entidad `Producto`.

```python
from servicios.servicio_producto import ServicioProducto

servicio = ServicioProducto()

# Listar todos
productos = servicio.obtener_todos()

# Buscar por ID (lanza ValueError si no existe)
prod = servicio.obtener_por_id(1)

# Insertar nuevo
servicio.guardar({
    "nombre": "Monitor 24\"",
    "descripcion": "Full HD 75Hz",
    "cantidad": 10,
    "precio": 299.99,
    "categoria_id": 1
})

# Actualizar existente
servicio.guardar({
    "id": 1,
    "nombre": "Monitor 27\"",
    "descripcion": "Full HD 144Hz",
    "cantidad": 5,
    "precio": 399.99,
    "categoria_id": 1
})

# Eliminar
servicio.borrar(1)
```

| método | descripción |
|---|---|
| `obtener_todos()` | Retorna lista de todos los productos. |
| `obtener_por_id(id)` | Retorna el producto o lanza `ValueError` si no existe. |
| `guardar(datos)` | Valida nombre, precio y existencia de categoría antes de persistir. |
| `borrar(id)` | Verifica existencia y elimina el producto. |

## Notas

- `guardar()` detecta automáticamente si debe hacer `INSERT` o `UPDATE` según si `datos` incluye `id` o no.
- `ServicioProducto` verifica que la `categoria_id` exista en la base de datos antes de guardar, delegando en `ServicioCategoria`.
- Las validaciones son manejadas por el sub-módulo `validaciones/` y nunca llegan al repositorio datos sin validar.
