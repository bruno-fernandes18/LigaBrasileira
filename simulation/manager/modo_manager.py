"""Modo de gerenciamento do jogador."""

from ...core.entities.time import Time
from ...core.entities.partida import Partida
from ...core.entities.jogador import Jogador
from ...core.enums.posicao import Posicao
from ...persistence.save_system import SaveSystem

class ModoPlayer:
    """Permite controle de um time pelo jogador."""

    def __init__(self, time: Time) -> None:
        self.time = time
        self.escalacao: list[Jogador] | None = None

    def escolher_escalacao(self) -> None:
        """Seleciona automaticamente uma escalação 4-3-3."""
        jogadores = list(self.time.jogadores)
        if not jogadores:
            self.escalacao = []
            return

        def sort_key(j: Jogador) -> int:
            return getattr(j, "qualidade_geral", 0)

        goleiros = sorted([j for j in jogadores if j.posicao == Posicao.GOLEIRO], key=sort_key, reverse=True)
        zagueiros = sorted([j for j in jogadores if j.posicao in (Posicao.ZAGUEIRO, Posicao.LATERAL)], key=sort_key, reverse=True)
        meias = sorted([j for j in jogadores if j.posicao in (Posicao.VOLANTE, Posicao.MEIA)], key=sort_key, reverse=True)
        atacantes = sorted([j for j in jogadores if j.posicao == Posicao.ATACANTE], key=sort_key, reverse=True)

        escala = []
        if goleiros:
            escala.append(goleiros.pop(0))

        escala.extend(zagueiros[:4])
        escala.extend(meias[:3])
        escala.extend(atacantes[:3])

        if len(escala) < 11:
            restantes = [j for j in jogadores if j not in escala]
            escala.extend(sorted(restantes, key=sort_key, reverse=True)[: 11 - len(escala)])

        self.escalacao = escala[:11]

    def avancar_partida(self, partida: Partida) -> None:
        """Avança uma partida controlada."""
        partida.simular()

    def salvar(self, path: str) -> None:
        """Salva o estado atual do manager."""
        SaveSystem.salvar(path, self)

    @staticmethod
    def carregar(path: str) -> "ModoPlayer":
        """Carrega um manager salvo."""
        return SaveSystem.carregar(path)
