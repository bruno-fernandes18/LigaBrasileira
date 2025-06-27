from persistence.history import Historico


def test_registrar_campeonato():
    hist = Historico()
    hist.registrar_campeonato(2023, "Liga", "Time A")
    temporada = hist.temporadas[0]
    assert temporada.campeonatos["Liga"] == "Time A"
    assert "Liga" in temporada.trofeus_por_time["Time A"]


def test_registrar_artilheiro_e_classificacao():
    hist = Historico()
    hist.registrar_artilheiro(2024, "Liga", "Jogador X")
    hist.registrar_classificacao(2024, ["Time A", "Time B"])
    temporada = hist.temporadas[0]
    assert temporada.artilheiros["Liga"] == "Jogador X"
    assert temporada.classificacao == ["Time A", "Time B"]
