"""Implementação da Copa do Brasil."""

from __future__ import annotations

from datetime import timedelta
from pathlib import Path

from ...core.entities.copa import Copa
from ...core.entities.partida import Partida


class CopaDoBrasil(Copa):
    """Copa nacional em mata-mata com jogos de ida e volta."""

    def gerar_calendario(self) -> None:
        """Cria chaves em formato mata‑mata com partidas de ida e volta."""
        self.partidas.clear()
        if len(self.times) < 2:
            return

        rodada = 1
        times = list(self.times)
        while len(times) > 1:
            nova_rodada: list[Partida] = []
            for i in range(0, len(times), 2):
                casa = times[i]
                visitante = times[i + 1]
                data_ida = (
                    self.calendario.partidas[-1].data + timedelta(days=3)
                    if self.calendario.partidas
                    else self.calendario.data_inicio
                )
                partida_ida = Partida(casa, visitante, rodada, data_ida)
                self.calendario.adicionar_partida(partida_ida)
                self.partidas.append(partida_ida)

                data_volta = self.calendario.proxima_data_disponivel(
                    data_ida + timedelta(days=3)
                )
                partida_volta = Partida(visitante, casa, rodada, data_volta)
                self.calendario.adicionar_partida(partida_volta)
                self.partidas.append(partida_volta)

                nova_rodada.append(partida_ida)

            times = [p.time_casa for p in nova_rodada]
            rodada += 1

        self.rodadas_total = rodada - 1

    def simular_rodada(self, rodada: int) -> None:  # pragma: no cover - simple wrapper
        """Simula a rodada e celebra ao final se houver campeão."""
        super().simular_rodada(rodada)

        if getattr(self, "rodadas_total", 0) != rodada:
            return

        finais = [p for p in self.partidas if p.rodada == rodada]
        if finais and all(p.concluida for p in finais):
            placares: dict[object, int] = {}
            for p in finais:
                placares[p.time_casa] = placares.get(p.time_casa, 0) + p.placar_casa
                placares[p.time_visitante] = placares.get(p.time_visitante, 0) + p.placar_visitante
            campeao = max(placares, key=placares.get)
            campeao.titulos += 1
            self._celebrar_campeao(campeao)

    def _celebrar_campeao(self, time) -> None:
        """Toca um hino simples caso ``pygame`` esteja disponível."""
        try:  # pragma: no cover - dependente de pygame
            import pygame

            arquivo = (
                Path(__file__).resolve().parents[2]
                / "gui"
                / "assets"
                / "sounds"
                / "crowd.mp3"
            )
            if arquivo.exists():
                pygame.mixer.init()
                pygame.mixer.music.load(str(arquivo))
                pygame.mixer.music.play()
        except Exception:
            pass

        print(f"{time.nome} é campeão da Copa do Brasil!")
