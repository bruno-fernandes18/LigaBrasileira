import random
from typing import List
from ..entidades.jogador import Jogador


def desenvolver_jogadores(jogadores: List[Jogador]):
    for jogador in jogadores:
        if jogador.idade < 25:
            jogador.desenvolver()


class PlayerDevelopmentEngine:
    """Motor de desenvolvimento de jogadores mais detalhado."""

    DEVELOPMENT_CURVES = {
        "early_peak": lambda age: max(0, 0.4 * (25 - abs(age - 22))),
        "normal": lambda age: max(0, 0.3 * (28 - abs(age - 25))),
        "late_bloomer": lambda age: max(0, 0.2 * (32 - abs(age - 28))),
    }

    def simulate_season_growth(self, player: Jogador):
        growth_factor = (
            0.6 * self._training_impact(player)
            + 0.3 * self._match_experience(player)
            + 0.1 * self._random_events(player)
        )

        curve = self.DEVELOPMENT_CURVES.get(player.development_profile, self.DEVELOPMENT_CURVES["normal"])
        age_factor = curve(player.idade)

        for attr in ["qualidade_ataque", "qualidade_meio_campo", "qualidade_defesa"]:
            improvement = growth_factor * age_factor * getattr(player, "potencial", 0)
            setattr(player, attr, min(99, getattr(player, attr) + improvement))

        if growth_factor > 1.8:
            self._trigger_breakthrough_event(player)

    # Métodos auxiliares simplificados -----------------------
    def _training_impact(self, player: Jogador) -> float:
        return player.potencial / 20

    def _match_experience(self, player: Jogador) -> float:
        return min(1.0, player.gols / 10)

    def _random_events(self, player: Jogador) -> float:
        return random.random()

    def _trigger_breakthrough_event(self, player: Jogador) -> None:
        player.potencial = min(99, player.potencial + 5)
