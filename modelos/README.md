# modelos

Módulo de modelos de datos del sistema de inventario. Define las entidades del dominio como dataclasses de Python.

## Estructura

```
modelos/
├── __init__.py
├── categoria.py
└── producto.py
```

## Clases

### `Categoria`

Representa una categoría de productos.

```python
from modelos.categoria import Categoria

nueva = Categoria(categoria="Electrónica")
existente = Categoria(categoria="Electrónica", id=1)
```

| atributo    | tipo       | descripción                                     |
|-------------|------------|-------------------------------------------------|
| nombre      | str        | Nombre de la categoría. Requerido.              |
| descripcion | str / None | Descripcion de la categoría. No requerido.      |
| id          | int / None | ID en la base de datos. None antes de insertar. |

---

### `Producto`

Representa un producto del inventario.

```python
from modelos.producto import Producto

nuevo = Producto(
    nombre="Monitor 24\"",
    descripcion="Full HD 75Hz",
    cantidad=10,
    precio=299.99,
    categoria_fk=1
)
```

| atributo    | tipo       | descripción                              |
|-------------|------------|------------------------------------------|
| nombre      | str        | Nombre del producto. Requerido.          |
| descripcion | str        | Descripción opcional del producto.       |
| cantidad    | int        | Stock disponible.                        |
| precio      | float      | Precio unitario.                         |
| categoria_id | int       | ID de la categoría asociada. Referencia a `categorias.id`. |
| id          | int / None | ID en la base de datos. None antes de insertar. |

## Notas

El campo `id` es `None` en instancias nuevas que todavía no fueron persistidas en la base de datos, y toma el valor del `INTEGER PRIMARY KEY` una vez insertadas.
