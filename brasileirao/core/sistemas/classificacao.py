from ..entidades.time import Time


def atualizar_factors_times(classificacao: list[Time]):
    for i, time in enumerate(classificacao):
        if i == 0:
            time.factor_torcida = min(20, time.factor_torcida + 3)
            time.factor_orcamento = min(20, time.factor_orcamento + 3)
            time.titulos += 1
        elif i < 4:
            time.factor_torcida = min(20, time.factor_torcida + 1)
            time.factor_orcamento = min(20, time.factor_orcamento + 1)
        elif i > len(classificacao) - 5:
            time.factor_torcida = max(0, time.factor_torcida - 2)
            time.factor_orcamento = max(0, time.factor_orcamento - 2)
        elif i > len(classificacao) - 9:
            time.factor_torcida = max(0, time.factor_torcida - 1)
            time.factor_orcamento = max(0, time.factor_orcamento - 1)
