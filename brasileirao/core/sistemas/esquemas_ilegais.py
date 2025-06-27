import random
from ..entidades.time import Time
from .financeiro import aplicar_multa_esquema


def verificar_esquema_apostas(time: Time) -> bool:
    if time.sorte == 20:
        return False
    chance = max(0.01, (20 - time.factor_torcida) * 0.02)
    if random.random() < chance:
        gravidade = random.choice([1, 2, 3, 4, 5])
        aplicar_punicao(time, gravidade)
        return True
    return False


def aplicar_punicao(time: Time, gravidade: int):
    time.factor_orcamento = max(0, time.factor_orcamento - gravidade)
    time.factor_torcida = max(0, time.factor_torcida - gravidade)
    aplicar_multa_esquema(time, gravidade)
