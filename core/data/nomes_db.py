"""Banco de dados de nomes."""

import random

NOMES_MASCULINOS = ["Joao", "Pedro", "Lucas"]
NOMES_FEMININOS = ["Maria", "Ana", "Juliana"]
SOBRENOMES = ["Silva", "Souza", "Oliveira"]


def gerar_nome(genero: str = 'M') -> str:
    """Gera um nome completo."""
    if genero == 'F':
        nome = random.choice(NOMES_FEMININOS)
    else:
        nome = random.choice(NOMES_MASCULINOS)
    return f"{nome} {random.choice(SOBRENOMES)}"
