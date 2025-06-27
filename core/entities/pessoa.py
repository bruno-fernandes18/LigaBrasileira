"""Entidade base Pessoa."""

class Pessoa:
    """Representa uma pessoa no sistema."""

    def __init__(self, nome: str, idade: int, nacionalidade: str) -> None:
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade
        self.aposentado = False
        self.reputacao = 15
        self.suspenso = False
        self.infracoes: list[dict] = []
        self.esquemas_envolvidos: list[str] = []

    def cometer_infracao(self, tipo: str, gravidade: int) -> None:
        """Registra uma infração e reduz reputação."""
        self.infracoes.append({"tipo": tipo, "gravidade": gravidade})
        self.reputacao = max(0, self.reputacao - gravidade)

    def verificar_aposentadoria(self) -> bool:
        """Verifica se a pessoa deve se aposentar."""
        return self.idade > 65 or (self.reputacao < 5 and self.idade > 40)
