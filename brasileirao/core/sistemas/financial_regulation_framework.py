from typing import List
from ..entidades.time import Time


def pagar_salarios_semanais(times: List[Time]):
    for time in times:
        time.pagar_salarios()


def aplicar_multa_esquema(time: Time, gravidade: int):
    multa_base = gravidade * 500_000
    multa_elenco = time.media_ataque * 100_000
    multa_torcida = time.factor_torcida * 50_000
    multa_total = multa_base + multa_elenco + multa_torcida
    time.orcamento -= multa_total
