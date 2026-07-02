# validaciones

Sub-módulo de validación dentro de `services`. Define el objeto de resultado de validación y las funciones validadoras por tipo de campo.

## Estructura

```
validaciones/
├── __init__.py
├── resultado_validacion.py
├── validadores_texto.py
└── validadores_numericos.py
```

## Clases

### `ResultadoValidacion`

Dataclass que representa el resultado de una validación. Es retornado por todos los validadores y consumido por `ServicioBase`.

| atributo | tipo       | descripción                                      |
|----------|------------|--------------------------------------------------|
| campo    | str        | Nombre del campo validado.                       |
| valido   | bool       | `True` si la validación pasó sin errores.        |
| errores  | list[str]  | Lista de mensajes de error. Vacía si es válido.  |

```python
from validaciones.resultado_validacion import ResultadoValidacion

resultado = ResultadoValidacion(campo="nombre", valido=False, errores=["No puede estar vacío."])
print(resultado)
# [nombre] -> Invalido
#  - No puede estar vacío.
```

---

## Funciones

### `validar_texto(texto, campo)` → `ResultadoValidacion`

Valida un campo de texto libre como nombres o descripciones.

```python
from validaciones.validadores_texto import validar_texto

resultado = validar_texto("Monitor Full HD", campo="nombre")
```

| regla | descripción |
|---|---|
| 1 | Debe ser `str`. |
| 2 | No puede estar vacío ni contener solo espacios. |
| 3 | Longitud entre 2 y 50 caracteres. |
| 4 | Solo letras (incluye tildes, ñ, ü), espacios, guiones y apóstrofes. |
| 5 | No puede empezar ni terminar con guion o apóstrofe. |

---

### `validar_precio(valor, campo)` → `ResultadoValidacion`

Valida un campo numérico de precio.

```python
from validaciones.validadores_numericos import validar_precio

resultado = validar_precio("299.99", campo="precio")
```

| regla | descripción |
|---|---|
| 1 | No puede contener símbolos. |
| 2 | No puede contener letras. |
| 3 | Debe ser un número positivo mayor a cero. |

## Notas

- Todos los validadores retornan `ResultadoValidacion` en vez de lanzar excepciones directamente. Es `ServicioBase` quien decide si lanzar un `ValueError` a partir del resultado.
- El campo `errores` acumula todos los errores encontrados, no solo el primero.
