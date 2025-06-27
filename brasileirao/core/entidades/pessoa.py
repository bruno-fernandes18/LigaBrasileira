"""Modela uma pessoa presente no campeonato."""


class Pessoa:
    """Entidade base para participantes da liga."""

    def __init__(self, nome: str, idade: int, nacionalidade: str) -> None:
        """Cria uma nova pessoa com atributos genéricos."""
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade
        self.aposentado = False
        self.reputacao = 15
        self.suspenso = False
        self.infracoes = []
        self.esquemas_envolvidos = []

    def cometer_infracao(self, tipo: str, gravidade: int) -> None:
        """Registra infração cometida pela pessoa."""

        self.infracoes.append({"tipo": tipo, "gravidade": gravidade})
        self.reputacao = max(0, self.reputacao - gravidade)

    def verificar_aposentadoria(self) -> bool:
        """Determina se a pessoa deve se aposentar."""

        return self.idade > 65 or (self.reputacao < 5 and self.idade > 40)
