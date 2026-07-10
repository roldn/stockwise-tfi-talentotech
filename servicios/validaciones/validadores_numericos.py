from .resultado_validacion import ResultadoValidacion
import re

def validar_precio(valor, campo:str = "precio") -> ResultadoValidacion:
    """
    Regla de Validacion - Campo de Precio:
        1. Debe ser int, float, o str convertible a float.
        2. Si es str, no puede estar vacío.
        3. Si es str, debe ser convertible a número válido.
        4. Debe ser mayor o igual a cero.
    """
    errores: list[str] = []

    # Regla 1 - Si ya es número, validar directamente sin conversión
    if isinstance(valor, (int, float)):
        # Regla 4 - Debe ser mayor o igual a cero
        if valor < 0:
            errores.append("El precio debe ser mayor o igual a cero.")
        return ResultadoValidacion(campo=campo, valido=not errores, errores=errores)

    # Regla 1 - Tipo incorrecto
    if not isinstance(valor, str):
        return ResultadoValidacion(campo=campo, valido=False, errores=[f"Se esperaba un número, se recibió {type(valor).__name__}."])

    valor = valor.strip()

    # Regla 2 - No puede estar vacío
    if not valor:
        return ResultadoValidacion(campo=campo, valido=False, errores=["El precio no puede estar vacío."])

    # Regla 3 - Debe ser convertible a número válido
    try:
        numero = float(valor)
    except ValueError:
        return ResultadoValidacion(campo=campo, valido=False, errores=["El precio debe ser un número válido."])

    # Regla 4 - Debe ser mayor o igual a cero
    if numero <= 0:
        errores.append("El precio debe ser mayor a cero.")

    return ResultadoValidacion(campo=campo, valido=not errores, errores=errores)
    
