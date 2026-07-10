# db

Módulo de base de datos para el sistema de inventario. Gestiona la conexión a SQLite, la creación del esquema y la configuración de rutas.

## Estructura

```
db/
├── __init__.py
├── config.py            # Constantes globales: ruta de la DB y menús
├── datos_iniciales.py   # Creación de datos iniciales
├── db_conexion.py       # Context manager para la conexión a SQLite
└── esquema.py           # Creación de tablas (ejecutar una sola vez)
```

## Archivos

### `config.py`
Define las constantes usadas en todo el proyecto: la ruta al archivo `.db` y las listas de opciones de los menús de productos y categorías.

### `db_conexion.py`
Provee el context manager `conexion()` que abre y cierra la conexión a SQLite de forma segura. Hace commit automático al salir del bloque `with` y rollback si ocurre una excepción. Las filas se retornan como objetos `sqlite3.Row`, accesibles por nombre de columna.

```python
from db.db_conexion import conexion

with conexion() as conn:
    resultado = conn.execute("SELECT * FROM productos").fetchall()
```

### `esquema.py`
Crea las tablas `categorias` y `productos` si no existen. Se ejecuta automaticamente desde `App.py`.

### `datos_iniciales.py`
Popula las tablas `categorias` y `productos` con datos pre-definidos. Se ejecuta automaticamente desde `App.py`.

## Tablas

**`categorias`**
| columna     | tipo    | restricciones             |
|-------------|---------|---------------------------|
| id          | INTEGER | PRIMARY KEY AUTOINCREMENT |
| nombre      | TEXT    | NOT NULL, UNIQUE          |
| descripcion | TEXT    | -                         |

**`productos`**
| columna      | tipo    | restricciones                          |
|--------------|---------|----------------------------------------|
| id           | INTEGER | PRIMARY KEY AUTOINCREMENT              |
| nombre       | TEXT    | NOT NULL                               |
| descripcion  | TEXT    | —                                      |
| cantidad     | REAL    | —                                      |
| precio       | REAL    | —                                      |
| categoria_id | INTEGER | FOREIGN KEY → categorias(id)           |

## Requisitos

- Python 3.10+
- sqlite3 (incluido en la librería estándar)
