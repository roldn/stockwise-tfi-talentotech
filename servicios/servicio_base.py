from servicios.validaciones.resultado_validacion import ResultadoValidacion

class ServicioBase:

    def _lanzar_error_si_resultado_es_invalido(self, resultado: ResultadoValidacion) -> None:
        """Lanza ValueError si el resultado de la validacion es invalido."""
        if not resultado.valido:
            raise ValueError(str(resultado))
