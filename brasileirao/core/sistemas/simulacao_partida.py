import random
from ..entidades.partida import Partida
from .sound_manager import SoundManager

class SimuladorPartida:
    def __init__(self, partida: Partida):
        self.partida = partida
        self.max_phases = random.randint(10, 20)

    def simular(self):
        gols_casa = random.randint(0, 3)
        gols_vis = random.randint(0, 3)
        for _ in range(gols_casa):
            self.partida.placar_casa += 1
            SoundManager.play("gol")
            if self.partida.time_casa.nome == "Flamengo":
                SoundManager.play("hino_flamengo")
        for _ in range(gols_vis):
            self.partida.placar_visitante += 1
            SoundManager.play("gol")
            if self.partida.time_visitante.nome == "Flamengo":
                SoundManager.play("hino_flamengo")
        for phase in range(self.max_phases):
            self.partida.adicionar_fase({"numero": phase})
        self.partida.finalizar()
