"""Ferramentas para simular uma temporada completa.

Este módulo provê a classe :class:`SimuladorTemporada`, responsável por
executar rodadas de todas as competições cadastradas e aplicar eventos
de mercado e de jogo a cada semana.
"""

from __future__ import annotations

from typing import List

from core.entities.competicao import Competicao
from core.entities.time import Time
from core.entities.jogador import Jogador
from core.enums.posicao import Posicao
from core.entities.liga import Liga
from core.systems.sistema_classificacao import atualizar_factors_times
from core.systems.sistema_eventos import (
    verificar_demissao_tecnicos,
    verificar_lesoes,
)
from core.systems.sistema_financeiro import (
    pagar_salarios_semanais,
    resolver_bancarrota,
)
from core.systems.sistema_regens import regenerar_jogadores


class SimuladorTemporada:
    """Executa rodadas e gerencia eventos sazonais.

    Args:
        competicoes (List[Competicao]): Lista de competições que farão
            parte da temporada.
    """

    def __init__(self, competicoes: List[Competicao]) -> None:
        """Inicializa o simulador.

        Args:
            competicoes: Competições que serão simuladas.
        """
        self.competicoes = competicoes
        self.rodada_atual = 1
        self.times: List[Time] = []
        for comp in competicoes:
            for t in comp.times:
                if t not in self.times:
                    self.times.append(t)

    def executar_rodada(self) -> None:
        """Simula a rodada atual.

        Executa as partidas de cada competição e em seguida aplica os
        sistemas de eventos e finanças. Ao final a rodada é
        incrementada.
        """
        for comp in self.competicoes:
            comp.simular_rodada(self.rodada_atual)
            if isinstance(comp, Liga):
                atualizar_factors_times(comp)

        jogadores = [j for t in self.times for j in t.jogadores]
        verificar_lesoes(jogadores)
        verificar_demissao_tecnicos(self.times)
        pagar_salarios_semanais(self.times)
        for t in self.times:
            if t.bancarrota:
                outros = [o for o in self.times if o is not t]
                resolver_bancarrota(t, outros)

        regenerar_jogadores(jogadores)
        self._mercado_transferencias()

        self.rodada_atual += 1

    def _mercado_transferencias(self) -> None:
        """Realiza transferências simples entre times.

        Este método cria negociações básicas para manter os elencos
        equilibrados ao longo da temporada.
        """
        for comprador in self.times:
            if comprador.orcamento <= 0:
                continue
            vendedores = [t for t in self.times if t is not comprador and t.jogadores]
            if not vendedores:
                continue
            vendedor = vendedores[0]
            jogador = vendedor.jogadores[0]
            valor = jogador.valor_mercado()
            if comprador.orcamento >= valor:
                vendedor.jogadores.remove(jogador)
                comprador.jogadores.append(jogador)
                comprador.orcamento -= valor
                vendedor.orcamento += valor
                jogador.time = comprador
                break
            else:
                if comprador.orcamento > 1_000_000:
                    novo = Jogador("Reforço", 20, "Brasil", Posicao.ATACANTE)
                    novo.time = comprador
                    comprador.jogadores.append(novo)
                    comprador.orcamento -= 1_000_000


def main() -> None:
    """Executa uma simulação simples via linha de comando."""
    liga = Liga("Demo", 2023)
    liga.times = [
        Time("Time A", "A", 1900, "Cidade A", "Estádio A"),
        Time("Time B", "B", 1900, "Cidade B", "Estádio B"),
    ]
    for t in liga.times:
        t.liga = liga
    liga.gerar_calendario()
    sim = SimuladorTemporada([liga])
    sim.executar_rodada()
    print(f"Placar: {liga.partidas[0].placar_casa}x{liga.partidas[0].placar_visitante}")


if __name__ == "__main__":
    main()
