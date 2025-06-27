"""Sistemas adicionais e utilidades da simulacao."""

from .sound_manager import SoundManager
from .simulation_engine import (
    calcular_phases,
    Rolagem,
    processar_bancarrota,
    CalendarioAvancado,
    CalendarioApocalipticoError,
    SalaTrofeus,
    LigaSimples,
    JogadorBase,
)
from .competitive_integrity_system import SportsIntegrityAgency
from .career_development_module import PlayerDevelopmentEngine
from .global_transfer_market import GlobalTransferMarket
from .career_termination_handler import CareerTerminationHandler

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
    "SportsIntegrityAgency",
    "PlayerDevelopmentEngine",
    "GlobalTransferMarket",
    "CareerTerminationHandler",
]
