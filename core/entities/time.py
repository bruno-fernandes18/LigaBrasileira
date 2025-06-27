"""Entidade Time."""

from __future__ import annotations
from typing import List

class Time:
    """Representa um clube de futebol."""

    def __init__(self, nome: str, apelido: str, fundacao: int, cidade: str, estadio: str) -> None:
        self.nome = nome
        self.apelido = apelido
        self.fundacao = fundacao
        self.cidade = cidade
        self.estadio = estadio
        self.liga = None
        self.jogadores: List['Jogador'] = []
        self.tecnico = None
        self.factor_torcida = 10
        self.factor_orcamento = 10
        self.sorte = 10
        self.pontos = 0
        self.saldo_gols = 0
        self.titulos = 0
        self.rivais: list[str] = []
        self.media_ataque = 0
        self.media_meio = 0
        self.media_defesa = 0
        self.esquemas_envolvidos: list[str] = []
        self.orcamento = 10_000_000
        self.despesas_salariais = 0
        self.bancarrota = False

    def calcular_medias(self) -> None:
        """Calcula médias de atributos dos jogadores."""
        if not self.jogadores:
            self.media_ataque = self.media_meio = self.media_defesa = 0
            return
        self.media_ataque = sum(j.qualidade_ataque for j in self.jogadores) / len(self.jogadores)
        self.media_meio = sum(j.qualidade_meio_campo for j in self.jogadores) / len(self.jogadores)
        self.media_defesa = sum(j.qualidade_defesa for j in self.jogadores) / len(self.jogadores)
