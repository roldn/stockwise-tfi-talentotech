# ui

Módulo de interfaz gráfica del sistema de inventario. Contiene la ventana principal, la barra de navegación y todos los componentes y vistas de la aplicación.

## Estructura

```
ui/
├── __init__.py
├── app.py
├── barra_navegacion.py
├── vistas/
│   ├── __init__.py
│   ├── vista_productos.py
│   └── vista_categorias.py
└── componentes/
    ├── __init__.py
    ├── tabla.py
    └── formularios/
        ├── __init__.py
        ├── formulario_producto.py
        └── formulario_categoria.py
```

## Clases

### `App`

Ventana raíz de la aplicación (`tk.Tk`). Inicializa la interfaz, registra las vistas y gestiona la navegación entre ellas.

```python
from ui.app import App

app = App()
app.mainloop()
```

**Comportamiento:**

- Título: `StockFlow`, tamaño inicial `960x600`, mínimo `800x500`.
- Las vistas se apilan con `grid` y se intercambian con `tkraise`.
- Al cambiar de vista llama a `actualizar()` para refrescar los datos.
- Abre por defecto en `VistaProductos`.

---

### `BarraNavegacion`

Barra de navegación superior con acceso a cada sección de la aplicación.

**Comportamiento:**

- Muestra el nombre `StockFlow` como branding a la izquierda.
- Un botón por cada vista registrada en `VISTAS`.
- El botón de la vista activa se resalta visualmente con `relief="sunken"` y fondo azul claro.
- Al clickear un botón notifica a `App` via el callback `mostrar_vista`.

---

## Sub-módulos

| carpeta       | descripción                                                             |
|---------------|-------------------------------------------------------------------------|
| `vistas/`     | Frames principales por sección. Ver [vistas/README.md](vistas/README.md). |
| `componentes/`| Widgets reutilizables y formularios modales. Ver [componentes/README.md](componentes/README.md). |

## Notas

- La capa `ui` no accede directamente a repositorios ni a la base de datos. Toda operación de datos pasa por la capa `servicios/`.
- Agregar una nueva sección requiere crear una vista en `vistas/`, registrarla en `BarraNavegacion.VISTAS` y en el loop de inicialización de `App._construir_ui`.
