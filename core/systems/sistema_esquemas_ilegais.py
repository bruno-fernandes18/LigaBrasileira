"""Verificação de esquemas ilegais."""

from ..entities.time import Time


def verificar_esquema_apostas(time: Time) -> bool:
    """Retorna True se um esquema for detectado."""
    return 'apostas' in time.esquemas_envolvidos


def aplicar_punicao(time: Time, gravidade: int) -> None:
    """Aplica punição de acordo com a gravidade."""
    time.factor_orcamento = max(0, time.factor_orcamento - gravidade)
    time.factor_torcida = max(0, time.factor_torcida - gravidade)
    time.orcamento -= gravidade * 1_000_000
