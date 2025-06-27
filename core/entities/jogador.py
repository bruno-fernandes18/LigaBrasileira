"""Entidade Jogador."""

from .pessoa import Pessoa
from ..enums.posicao import Posicao

class Jogador(Pessoa):
    """Representa um atleta."""

    def __init__(self, nome: str, idade: int, nacionalidade: str, posicao: Posicao) -> None:
        super().__init__(nome, idade, nacionalidade)
        self.posicao = posicao
        self.qualidade_ataque = 0
        self.qualidade_meio_campo = 0
        self.qualidade_defesa = 0
        self.qualidade_geral = 0
        self.potencial = 0
        self.gols = 0
        self.assistencias = 0
        self.cartoes_amarelos = 0
        self.cartoes_vermelhos = 0
        self.lesoes: list[dict] = []
        self.titulos = 0
        self.time = None

    def calcular_qualidade_geral(self) -> None:
        """Calcula qualidade geral conforme posição."""
        if self.posicao == Posicao.ATACANTE:
            self.qualidade_geral = int(0.7 * self.qualidade_ataque + 0.3 * self.qualidade_meio_campo)
        elif self.posicao == Posicao.MEIA:
            self.qualidade_geral = int(0.5 * self.qualidade_meio_campo + 0.3 * self.qualidade_ataque + 0.2 * self.qualidade_defesa)
        else:
            self.qualidade_geral = int(0.6 * self.qualidade_defesa + 0.4 * self.qualidade_meio_campo)

    def valor_mercado(self) -> int:
        """Retorna valor estimado do jogador."""
        base = self.qualidade_geral * 500_000
        if self.idade < 22:
            base *= 1.5
        if self.idade > 30:
            base *= 0.7
        return int(base * (self.potencial / 20))
