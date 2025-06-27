"""Sistemas adicionais e utilidades da simulacao."""

from .sound_manager import SoundManager
from .barroso import (
    calcular_phases,
    Rolagem,
    processar_bancarrota,
    CalendarioAvancado,
    CalendarioApocalipticoError,
    SalaTrofeus,
    LigaSimples,
    JogadorBase,
)

__all__ = [
    "SoundManager",
    "calcular_phases",
    "Rolagem",
    "processar_bancarrota",
    "CalendarioAvancado",
    "CalendarioApocalipticoError",
    "SalaTrofeus",
    "LigaSimples",
    "JogadorBase",
]
