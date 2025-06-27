"""Banco de dados de nomes."""

import random

NOMES_MASCULINOS = [
    "Joao",
    "Pedro",
    "Lucas",
    "Carlos",
    "Marcos",
    "Rafael",
    "Felipe",
    "Roberto",
    "Gustavo",
    "Bruno",
    "Fernando",
    "Thiago",
    "Diego",
    "Ricardo",
    "Anderson",
    "Eduardo",
    "Leonardo",
    "Paulo",
    "Miguel",
    "Antônio",
    "Luiz",
    "Fábio",
    "Henrique",
    "Matheus",
    "Daniel",
    "Luan",
    "Alex",
    "Rodrigo",
    "Sergio",
    "Marcelo",
]

NOMES_FEMININOS = [
    "Maria",
    "Ana",
    "Juliana",
    "Patricia",
    "Fernanda",
    "Camila",
    "Tatiana",
    "Leticia",
    "Bruna",
    "Juliana",
    "Aline",
    "Carolina",
    "Mariana",
    "Jessica",
    "Sabrina",
    "Larissa",
    "Isabela",
    "Paula",
    "Cristina",
    "Carla",
    "Luana",
    "Daniela",
    "Renata",
    "Adriana",
]

SOBRENOMES = [
    "Silva",
    "Souza",
    "Oliveira",
    "Costa",
    "Pereira",
    "Ferreira",
    "Rodrigues",
    "Almeida",
    "Nascimento",
    "Gomes",
    "Ribeiro",
    "Alves",
    "Vieira",
    "Barbosa",
    "Lima",
    "Moura",
    "Dias",
]


def gerar_nome(genero: str = 'M') -> str:
    """Gera um nome completo."""
    if genero == 'F':
        nome = random.choice(NOMES_FEMININOS)
    else:
        nome = random.choice(NOMES_MASCULINOS)
    return f"{nome} {random.choice(SOBRENOMES)}"
