"""Simulação básica de uma temporada."""

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
from core.systems.sistema_financeiro import pagar_salarios_semanais
from core.systems.sistema_regens import regenerar_jogadores


class SimuladorTemporada:
    """Executa rodadas e gerencia eventos sazonais."""

    def __init__(self, competicoes: List[Competicao]) -> None:
        self.competicoes = competicoes
        self.rodada_atual = 1
        self.times: List[Time] = []
        for comp in competicoes:
            for t in comp.times:
                if t not in self.times:
                    self.times.append(t)

    def executar_rodada(self) -> None:
        """Simula a rodada atual em todas as competições."""
        for comp in self.competicoes:
            comp.simular_rodada(self.rodada_atual)
            if isinstance(comp, Liga):
                atualizar_factors_times(comp)

        jogadores = [j for t in self.times for j in t.jogadores]
        verificar_lesoes(jogadores)
        verificar_demissao_tecnicos(self.times)
        pagar_salarios_semanais(self.times)
        regenerar_jogadores(jogadores)
        self._mercado_transferencias()

        self.rodada_atual += 1

    def _mercado_transferencias(self) -> None:
        """Realiza transferências simples entre times."""
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
                break

