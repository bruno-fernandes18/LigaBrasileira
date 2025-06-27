"""Entidade Tecnico."""

from .pessoa import Pessoa
from ..enums.estilo_tatico import EstiloTatico

class Tecnico(Pessoa):
    """Representa um técnico de futebol."""

    def __init__(self, nome: str, idade: int, nacionalidade: str) -> None:
        super().__init__(nome, idade, nacionalidade)
        self.estilo_tatico = EstiloTatico.BALANCEADO
        self.qualidade_ataque = 0
        self.qualidade_meio_campo = 0
        self.qualidade_defesa = 0
        self.derrotas_consecutivas = 0
        self.time = None
        self.titulos = 0

    def demitir(self) -> None:
        """Remove o técnico do time."""
        if self.time:
            self.time.tecnico = None
            self.time = None
        self.derrotas_consecutivas = 0
