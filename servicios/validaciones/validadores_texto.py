from servicios.validaciones.resultado_validacion import ResultadoValidacion
import re

TXT_MIN = 2
TXT_MAX = 50

PATRON_TXT = re.compile(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s\-']+$")

def validar_texto(texto: str, campo:str = 'nombre') -> ResultadoValidacion:
    """
    Regla de Validacion - Campo de Texto:
    
        1. Debe ser str
        2. No puede estar vacio ni ser solo espacio
        3. Longitud: entre TXT_MIN y TXT_MAX caracteres
        4. Solo letras (incluye tildes, ñ, ü), espacios, guiones, y apostrofes.
        5. No puede empezar ni terminar con espacios, guion, o apostrofes.
    """
    
    errores: list[str] = []

    # Regla 1 - Tipo correcto
    if not isinstance(texto, str):
        errores.append(f"Se esperaba una cadena de texto, se recibio {type(texto).__name__}")

    valor = texto.strip()

    # Regla 2 - No ser un input vacio
    if not valor:
        errores.append("El campo no puede estar vacio ni tener solo espacios.")

    # Regla 3 - Longitud
    if len(valor) < TXT_MIN:
        errores.append(f"Demasiado corto: minimo {TXT_MIN} caracteres, se recibieron {len(valor)}")
    if len(valor) > TXT_MAX:
        errores.append(f"Demasiado largo: minimo {TXT_MIN} caracteres, se recibieron {len(valor)}")

    # Regla 4 - Caracteres validos
    if not PATRON_TXT.match(valor):
        if re.search(r"[0-9]", valor):
            errores.append("No puede contener numeros.")
        else:
            caracteres_invalidos = set(re.findall(r"[^a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s\-']", valor))
            errores.append(f"Caracteres no permitidos: {', '.join(sorted(caracteres_invalidos))}")

    # Regla 5 - No empezar ni terminar con caracteres especiales
    if valor and valor[0] in ("-", "'"):
        errores.append("No puede empezar con guion o apostrofe.")
    if valor and valor[-1] in ("-", "'"):
        errores.append("No puede terminar con guion o apostrofe.")

    return ResultadoValidacion(campo=campo, valido=not errores, errores=errores)
