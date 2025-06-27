from enum import Enum

class Posicao(Enum):
    """Posições de jogadores em campo."""
    GOLEIRO = 1
    LATERAL = 2
    ZAGUEIRO = 3
    VOLANTE = 4
    MEIA = 5
    ATACANTE = 6
