from typing import List
from .time import Time
from .partida import Partida
from .calendario import Calendario

class Competicao:
    def __init__(self, nome: str, temporada: int):
        self.nome = nome
        self.temporada = temporada
        self.times: List[Time] = []
        self.partidas: List[Partida] = []
        self.classificacao: List[Time] = []
        self.artilharia = []
        self.assistencias = []
        self.dependente_de = None
        self.calendario = Calendario()
        self.trofeu = None
        self.concluida = False

    def adicionar_time(self, time: Time):
        self.times.append(time)

    def gerar_calendario(self):
        """Gera o calendario de jogos no formato ida e volta."""
        from datetime import timedelta

        self.partidas.clear()
        if len(self.times) < 2:
            return

        times = list(self.times)
        # Se numero impar de times, adiciona um bye (None)
        if len(times) % 2 == 1:
            times.append(None)

        n = len(times)
        rodadas_primeira_fase = n - 1
        calendario_rodadas: List[List[tuple[Time, Time]]] = []

        # Algoritmo do metodo "circle" para round-robin
        for r in range(rodadas_primeira_fase):
            pares = []
            for i in range(n // 2):
                t1 = times[i]
                t2 = times[n - 1 - i]
                if t1 is not None and t2 is not None:
                    pares.append((t1, t2))
            calendario_rodadas.append(pares)
            # rotaciona preservando o primeiro elemento
            times = [times[0]] + [times[-1]] + times[1:-1]

        # Segunda fase (jogos de volta)
        calendario_rodadas += [[(b, a) for (a, b) in rodada] for rodada in calendario_rodadas]

        data = self.calendario.data_inicio
        for numero, jogos in enumerate(calendario_rodadas, start=1):
            for casa, fora in jogos:
                partida = Partida(casa, fora, numero, data)
                self.calendario.adicionar_partida(partida)
                self.partidas.append(partida)
            data += timedelta(days=7)

    def simular_rodada(self, numero: int):
        """Simula todas as partidas de uma rodada."""
        from ..sistemas.simulacao_partida import SimuladorPartida

        for partida in self.partidas:
            if partida.rodada == numero and not partida.concluida:
                SimuladorPartida(partida).simular()
        self.atualizar_classificacao()

    def atualizar_classificacao(self):
        self.classificacao = sorted(
            self.times,
            key=lambda t: (t.pontos, t.saldo_gols),
            reverse=True,
        )

    def simular_partidas(self):
        for partida in self.partidas:
            if not partida.concluida:
                partida.simular()

    def definir_campeao(self, time: Time):
        time.titulos += 1
        if self.trofeu:
            self.trofeu.conceder(time)
