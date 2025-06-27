from __future__ import annotations
from typing import List
from ..enums.setor import Setor

class Time:
    def __init__(self, nome: str, apelido: str, fundacao: int, cidade: str, estadio: str):
        self.nome = nome
        self.apelido = apelido
        self.fundacao = fundacao
        self.cidade = cidade
        self.estadio = estadio
        self.jogadores: List['Jogador'] = []
        self.tecnico = None
        self.factor_torcida = 10
        self.factor_orcamento = 10
        self.sorte = 10
        self.pontos = 0
        self.saldo_gols = 0
        self.titulos = 0
        self.media_ataque = 0
        self.media_meio = 0
        self.media_defesa = 0
        self.esquemas_envolvidos = []
        self.orcamento = 10_000_000
        self.salarios: List[int] = []
        self.rivais = []

    def calcular_medias(self):
        if self.jogadores:
            self.media_ataque = sum(j.qualidade_ataque for j in self.jogadores) / len(self.jogadores)
            self.media_meio = sum(j.qualidade_meio_campo for j in self.jogadores) / len(self.jogadores)
            self.media_defesa = sum(j.qualidade_defesa for j in self.jogadores) / len(self.jogadores)

    def setor_mais_fraco(self) -> Setor:
        medias = {
            Setor.ATAQUE: self.media_ataque,
            Setor.MEIO_CAMPO: self.media_meio,
            Setor.DEFESA: self.media_defesa,
        }
        return min(medias, key=medias.get)

    def pagar_salarios(self):
        total_salarios = sum(self.salarios)
        self.orcamento -= total_salarios
        if self.orcamento < 0:
            self.entrar_bancarrota()

    def entrar_bancarrota(self):
        self.jogadores.clear()
        self.orcamento = 0
        self.factor_orcamento = 5
        self.factor_torcida = 5
        self.sorte = 5
