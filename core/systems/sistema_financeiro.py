"""Sistema financeiro."""

from ..entities.time import Time


def pagar_salarios_semanais(times: list[Time]) -> None:
    """Deduz despesas salariais do orçamento."""
    for time in times:
        time.orcamento -= time.despesas_salariais
        if time.orcamento < 0:
            time.bancarrota = True
