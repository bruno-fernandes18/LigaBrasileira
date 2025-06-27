class Historico:
    def __init__(self):
        self.temporadas = []

    def adicionar_temporada(self, temporada: dict):
        self.temporadas.append(temporada)

    def obter_trofeus_time(self, time: str):
        return [t for t in self.temporadas if t.get('campeao') == time]

    def obter_detalhes_temporada(self, ano: int):
        for temp in self.temporadas:
            if temp.get('ano') == ano:
                return temp
        return None
