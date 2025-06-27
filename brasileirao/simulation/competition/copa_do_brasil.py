from ...core.entidades.copa import Copa


class CopaDoBrasil(Copa):
    """Copa do Brasil com fases eliminatórias."""

    def selecionar_participantes(self, times):
        self.times = times[:]
        self.gerar_calendario()
