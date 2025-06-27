from ...core.entidades.liga import Liga


class LigaBrasileira(Liga):
    """Implementação simples da liga nacional."""

    def preparar_temporada(self):
        self.gerar_calendario()
        self.atualizar_classificacao()
