# repositorios

Módulo de acceso a datos del sistema de inventario. Implementa el Repository Pattern usando una clase base abstracta y una subclase por entidad.

## Estructura

```
repositorios/
├── __init__.py
├── repositorio_base.py
├── repositorio_categorias.py
└── repositorio_productos.py
```

## Clases

### `RepositorioBase` (ABC)

Clase abstracta que define las operaciones comunes a todas las entidades. No se instancia directamente.

| método | descripción |
|---|---|
| `tabla` | Propiedad abstracta. Cada subclase retorna el nombre de su tabla. |
| `_from_row(fila)` | Método abstracto. Convierte un `sqlite3.Row` al modelo correspondiente. |
| `obtener_por_id(id)` | Retorna el objeto con ese ID o `None` si no existe. |
| `obtener_todos()` | Retorna una lista con todos los registros de la tabla. |
| `borrar(id)` | Elimina el registro con ese ID. |

---

### `RepositorioCategoria`

Maneja el acceso a la tabla `categorias`.

```python
from repositorios.repositorio_categorias import RepositorioCategoria
from modelos.categoria import Categoria

repo = RepositorioCategoria()

# Insertar
repo.guardar(Categoria(categoria="Electrónica"))

# Actualizar
repo.guardar(Categoria(id=1, categoria="Electrónica y tecnología"))

# Buscar
cat = repo.obtener_por_id(1)

# Listar
todas = repo.obtener_todos()

# Eliminar
repo.borrar(1)
```

---

### `RepositorioProducto`

Maneja el acceso a la tabla `productos`.

```python
from repositorios.repositorio_productos import RepositorioProducto
from modelos.producto import Producto

repo = RepositorioProducto()

# Insertar
repo.guardar(Producto(
    nombre="Monitor 24\"",
    descripcion="Full HD 75Hz",
    cantidad=10,
    precio=299.99,
    categoria_fk=1
))

# Actualizar
repo.guardar(Producto(
    id=1,
    nombre="Monitor 27\"",
    descripcion="Full HD 144Hz",
    cantidad=5,
    precio=399.99,
    categoria_id=1
))

# Buscar
prod = repo.obtener_por_id(1)

# Listar
todos = repo.obtener_todos()

# Eliminar
repo.borrar(1)
```

## Notas

- El método `guardar()` detecta automáticamente si debe hacer `INSERT` o `UPDATE` según si `id` es `None` o no.
- Todas las operaciones usan el context manager `conexion()` del módulo `db`, que garantiza commit automático y rollback ante excepciones.
