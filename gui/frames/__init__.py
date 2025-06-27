"""Subpacote contendo frames da interface gráfica."""

from .main_menu_frame import MainMenuFrame
from .manager_frame import ManagerFrame
from .classificacao_frame import ClassificacaoFrame
from .partida_frame import PartidaFrame
from .historico_frame import HistoricoFrame
from .financas_frame import FinancasFrame
from .mercado_transferencias_frame import MercadoTransferenciasFrame

__all__ = [
    "MainMenuFrame",
    "ManagerFrame",
    "ClassificacaoFrame",
    "PartidaFrame",
    "HistoricoFrame",
    "FinancasFrame",
    "MercadoTransferenciasFrame",
]
