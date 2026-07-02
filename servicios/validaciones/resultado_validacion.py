from dataclasses import dataclass, field

@dataclass
class ResultadoValidacion:
    campo: str
    valido: bool
    errores: list[str] = field(default_factory=list)

    def __str__(self) -> str:
        estado = "Valido" if self.valido else "Invalido"
        base = f"[{self.campo}] -> {estado}"
        if self.errores:
            detalle = "\n".join(f" - {e}" for e in self.errores)
            return f"{base}\n{detalle}"
        return base
