class TimesDB:
    TIMES_BRASILEIRO_A = ['Flamengo', 'Palmeiras', 'Santos']
    TIMES_BRASILEIRO_B = ['Vasco', 'Cruzeiro', 'Botafogo']

    @staticmethod
    def obter_time(nome: str):
        if nome in TimesDB.TIMES_BRASILEIRO_A + TimesDB.TIMES_BRASILEIRO_B:
            return {'nome': nome}
        return None
