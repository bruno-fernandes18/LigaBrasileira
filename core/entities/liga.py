"""Entidade Liga."""

from .competicao import Competicao

class Liga(Competicao):
    """Liga em formato de pontos corridos."""

    def gerar_calendario(self) -> None:
        super().gerar_calendario()
        self.classificacao = self.times[:]
