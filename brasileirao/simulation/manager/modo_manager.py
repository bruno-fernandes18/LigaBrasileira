from ...core.entidades.time import Time
from ...core.entidades.partida import Partida


class ModoPlayer:
    """Modo simplificado para controlar um time."""

    def __init__(self, time: Time):
        self.time = time

    def avancar_partida(self, partida: Partida):
        partida.finalizar()
