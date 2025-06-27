class RivaisDB:
    RIVAIS = {
        'Flamengo': ['Fluminense', 'Vasco', 'Botafogo'],
        'Corinthians': ['Palmeiras', 'Sao Paulo', 'Santos'],
    }

    @staticmethod
    def obter_rivais(time: str):
        return RivaisDB.RIVAIS.get(time, [])
