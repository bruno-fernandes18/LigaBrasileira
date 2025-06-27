from enum import Enum
from .posicao import Posicao

class Setor(Enum):
    DEFESA = 1
    MEIO_CAMPO = 2
    ATAQUE = 3

    def posicoes(self):
        if self == Setor.DEFESA:
            return [Posicao.GOLEIRO, Posicao.ZAGUEIRO, Posicao.LATERAL]
        if self == Setor.MEIO_CAMPO:
            return [Posicao.VOLANTE, Posicao.MEIA]
        if self == Setor.ATAQUE:
            return [Posicao.ATACANTE]
        return []
