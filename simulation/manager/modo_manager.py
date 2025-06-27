"""Modo de gerenciamento do jogador."""

from ...core.entities.time import Time
from ...core.entities.partida import Partida

class ModoPlayer:
    """Permite controle de um time pelo jogador."""

    def __init__(self, time: Time) -> None:
        self.time = time

    def escolher_escalacao(self) -> None:
        """Método placeholder para escolha de escalação."""
        pass

    def avancar_partida(self, partida: Partida) -> None:
        """Avança uma partida controlada."""
        partida.simular()
