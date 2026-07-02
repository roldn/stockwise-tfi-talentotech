from resultado_validacion import ResultadoValidacion
import re

def validar_precio(valor, campo:str = "precio") -> ResultadoValidacion:
    
    """
        Validaciones - Campo de Texto:
    
        Reglas:
            1. Debe ser un numero (in o float).
            2. debe ser positivo.
            3. No puede ser cero. 
    """

    errores: list[str] = []

    contiene_simbolos = re.compile(r"[^a-zA-Z0-9]")
    contiene_letras = re.compile(r"[a-zA-Z]")

    if contiene_simbolos.search(valor):
        errores.append(f"El precio no puede contener simbolos")
    
    if contiene_letras.search(valor):
        errores.append(f"El precio no puede contener letras")

    if not errores:
        valor = float(valor)
        if valor == 0 or valor < 0 :
            errores.append("El precio debe ser un numero positivo y mayor a cero.")

    return ResultadoValidacion(
        campo=campo,
        valido=not errores,
        errores=errores
    )
    
