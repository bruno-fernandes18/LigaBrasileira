"""Tipos de competições disponíveis para simulação."""

from .liga_brasileira import LigaBrasileira
from .liga_segunda_divisao import LigaSegundaDivisao
from .copa_do_brasil import CopaDoBrasil

__all__ = [
    "LigaBrasileira",
    "LigaSegundaDivisao",
    "CopaDoBrasil",
]
