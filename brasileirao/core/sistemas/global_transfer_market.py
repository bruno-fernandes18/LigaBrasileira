import random
from typing import List
from ..entidades.time import Time
from ..enums.setor import Setor


def contratar_jogador(time_comprador: Time, time_vendedor: Time, setor: Setor) -> bool:
    chance = 0.6 - (time_vendedor.sorte * 0.01)
    if random.random() > chance:
        return False
    jogadores = [j for j in time_vendedor.jogadores if j.posicao in setor.posicoes()]
    if not jogadores:
        return False
    jogador = max(jogadores, key=lambda j: j.qualidade_geral)
    valor = jogador.valor_mercado()
    if time_comprador.factor_orcamento * 1_000_000 > valor:
        time_vendedor.jogadores.remove(jogador)
        time_comprador.jogadores.append(jogador)
        jogador.time = time_comprador
        return True
    return False


class GlobalTransferMarket:
    """Sistema de transferências com negociações dinâmicas."""

    def __init__(self) -> None:
        self.player_valuation_model = PlayerValuationAI()
        self.negotiation_engine = DynamicNegotiationSystem()

    def process_transfer(self, buyer: Time, seller: Time, player) -> None:
        base_value = self.player_valuation_model.calculate_value(player)
        negotiation_params = {
            "buyer_financial_power": buyer.factor_orcamento,
            "seller_financial_need": seller.factor_orcamento,
            "player_morale": getattr(player, "morale", 50),
            "media_pressure": MediaInfluenceSimulator.get_transfer_pressure(),
        }
        agreement = self.negotiation_engine.negotiate(
            base_value=base_value, parameters=negotiation_params
        )

        setattr(player, "morale", getattr(player, "morale", 50) + agreement["player_morale_impact"])
        buyer.factor_orcamento -= agreement["final_fee"] / 1_000_000
        seller.factor_orcamento += agreement["final_fee"] / 1_000_000

        MediaSystem.generate_headlines(
            player=player,
            fee=agreement["final_fee"],
            buying_club=buyer,
            selling_club=seller,
        )


class PlayerValuationAI:
    def calculate_value(self, player) -> int:
        return player.valor_mercado()


class DynamicNegotiationSystem:
    def negotiate(self, base_value: int, parameters: dict) -> dict:
        final_fee = int(base_value * (1 + random.random() * 0.1))
        return {
            "final_fee": final_fee,
            "player_morale_impact": random.randint(-5, 5),
        }


class MediaInfluenceSimulator:
    @staticmethod
    def get_transfer_pressure() -> int:
        return random.randint(0, 100)


class MediaSystem:
    @staticmethod
    def generate_headlines(**kwargs) -> None:
        pass  # placeholder
