from enum import Enum

class FasePartida(Enum):
    """Fases de uma partida."""
    MEIO_CAMPO = 1
    ATAQUE = 2
    DEFESA = 3
    GOL = 4
