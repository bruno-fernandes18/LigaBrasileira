from enum import Enum
from .posicao import Posicao

class Setor(Enum):
    """Setores do campo."""
    DEFESA = 1
    MEIO_CAMPO = 2
    ATAQUE = 3

    def posicoes(self) -> list[Posicao]:
        """Retorna as posições associadas ao setor."""
        if self == Setor.DEFESA:
            return [Posicao.GOLEIRO, Posicao.LATERAL, Posicao.ZAGUEIRO]
        if self == Setor.MEIO_CAMPO:
            return [Posicao.VOLANTE, Posicao.MEIA]
        if self == Setor.ATAQUE:
            return [Posicao.ATACANTE]
        return []
