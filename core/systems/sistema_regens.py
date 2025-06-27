"""Sistema de regeneração de jogadores."""

from ..entities.jogador import Jogador
from ..enums.posicao import Posicao


def regenerar_jogadores(jogadores: list[Jogador]) -> None:
    """Gera jogadores genéricos até que o total alcance 1000."""
    total = len(jogadores)
    while total < 1000:
        jogadores.append(Jogador("Regen", 17, "Brasil", Posicao.ATACANTE))
        total += 1
