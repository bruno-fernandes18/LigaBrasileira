"""Definição da entidade ``Jogador``."""

from .pessoa import Pessoa
from ..enums.posicao import Posicao

class Jogador(Pessoa):
    """Representa um atleta vinculado a um time."""

    def __init__(self, nome: str, idade: int, nacionalidade: str, posicao: Posicao) -> None:
        """Inicializa atributos do jogador."""

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
        self.lesoes = []
        self.titulos = 0
        self.time = None
        self.face_image = 'generic_0.png'

    def calcular_qualidade_geral(self) -> None:
        """Atualiza a avaliação de qualidade geral do jogador."""
        if self.posicao == Posicao.ATACANTE:
            self.qualidade_geral = int(0.7*self.qualidade_ataque + 0.2*self.qualidade_meio_campo + 0.1*self.qualidade_defesa)
        elif self.posicao == Posicao.MEIA:
            self.qualidade_geral = int(0.4*self.qualidade_ataque + 0.5*self.qualidade_meio_campo + 0.1*self.qualidade_defesa)
        elif self.posicao == Posicao.VOLANTE:
            self.qualidade_geral = int(0.2*self.qualidade_ataque + 0.5*self.qualidade_meio_campo + 0.3*self.qualidade_defesa)
        elif self.posicao in [Posicao.LATERAL, Posicao.ZAGUEIRO]:
            self.qualidade_geral = int(0.3*self.qualidade_ataque + 0.2*self.qualidade_meio_campo + 0.5*self.qualidade_defesa)
        else:
            self.qualidade_geral = self.qualidade_defesa

    def valor_mercado(self) -> int:
        base = self.qualidade_geral * 500_000
        if self.idade < 22:
            base *= 1.5
        if self.idade > 30:
            base *= 0.7
        return int(base * (self.potencial / 20))

    def desenvolver(self):
        if self.idade < 25:
            incremento = min(1.0, self.potencial / 20)
            if self.posicao == Posicao.ATACANTE:
                self.qualidade_ataque = min(20, self.qualidade_ataque + incremento)
            elif self.posicao == Posicao.MEIA:
                self.qualidade_meio_campo = min(20, self.qualidade_meio_campo + incremento)
            elif self.posicao in [Posicao.ZAGUEIRO, Posicao.GOLEIRO]:
                self.qualidade_defesa = min(20, self.qualidade_defesa + incremento)
            else:
                self.qualidade_defesa = min(20, self.qualidade_defesa + incremento*0.7)
                self.qualidade_meio_campo = min(20, self.qualidade_meio_campo + incremento*0.3)
            self.calcular_qualidade_geral()
