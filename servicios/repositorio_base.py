from .validaciones.resultado_validacion import Resultadovalidacion

class ServicioBase:

    def _lanzar_error_si_resultado_es_invalido(self, resultado: Resultadovalidacion) -> None:
        """Lanza ValueError si el resultado de la validacion es invalido."""
        if not resultado.valido:
            raise ValueError(str(resultado))
