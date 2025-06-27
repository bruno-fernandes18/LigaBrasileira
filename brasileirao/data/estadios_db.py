class EstadiosDB:
    ESTADIOS = {
        'Maracana': {
            'cidade': 'Rio de Janeiro',
            'capacidade': 78000,
            'imagem': 'maracana.png'
        },
    }

    @staticmethod
    def obter_estadio(nome: str):
        return EstadiosDB.ESTADIOS.get(nome, {})
