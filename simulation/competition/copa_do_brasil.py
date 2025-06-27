"""Implementação da Copa do Brasil."""

from ...core.entities.copa import Copa

class CopaDoBrasil(Copa):
    """Copa nacional em mata-mata."""

    def gerar_calendario(self) -> None:
        super().gerar_calendario()
