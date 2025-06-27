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
from core.systems.sistema_financeiro import pagar_salarios_semanais
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
        self.resultados: dict[str, list[str]] = {}

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

    def encerrar_temporada(self) -> None:
        """Registra os resultados finais das competições."""
        self.resultados.clear()
        for comp in self.competicoes:
            if isinstance(comp, Liga):
                comp.classificacao.sort(
                    key=lambda t: (t.pontos, t.saldo_gols), reverse=True
                )
            self.resultados[comp.nome] = [t.nome for t in getattr(comp, "classificacao", [])]

    def iniciar_nova_temporada(self, qtd_movimentacao: int = 4) -> None:
        """Avança o calendário promovendo e rebaixando equipes."""
        self.encerrar_temporada()
        try:
            from .competition.liga_brasileira import LigaBrasileira
            from .competition.liga_segunda_divisao import LigaSegundaDivisao
        except Exception:  # pragma: no cover - fallback for optional imports
            LigaBrasileira = LigaSegundaDivisao = None  # type: ignore

        liga_a = next(
            (c for c in self.competicoes if LigaBrasileira and isinstance(c, LigaBrasileira)),
            None,
        )
        liga_b = next(
            (c for c in self.competicoes if LigaSegundaDivisao and isinstance(c, LigaSegundaDivisao)),
            None,
        )
        if liga_a and liga_b:
            rebaixados = liga_a.classificacao[-qtd_movimentacao:]
            promovidos = liga_b.classificacao[:qtd_movimentacao]
            for t in rebaixados:
                liga_a.times.remove(t)
                liga_b.times.append(t)
                t.liga = liga_b
            for t in promovidos:
                liga_b.times.remove(t)
                liga_a.times.append(t)
                t.liga = liga_a

        self.times = []
        for comp in self.competicoes:
            comp.temporada += 1
            comp.gerar_calendario()
            for t in comp.times:
                if t not in self.times:
                    self.times.append(t)

        self.rodada_atual = 1


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
