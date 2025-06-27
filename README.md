![Coverage](https://github.com/example/LigaBrasileira/actions/workflows/ci.yml/badge.svg?branch=main)
# Liga Brasileira
![Build](https://github.com/example/LigaBrasileira/actions/workflows/ci.yml/badge.svg)

Simulador simples de competições do futebol brasileiro.

## Instalação

```bash
pip install -r requirements.txt
```

Certifique-se de que a biblioteca padrão **Tkinter** do Python esteja
disponível no seu ambiente, pois ela é necessária para a interface gráfica.

## Uso

### Modo GUI

Execute a aplicação gráfica baseada em Tkinter:

```bash
python app.py
```

### Modo CLI

Para uma simulação rápida diretamente no terminal:

```bash
python -m simulation.temporada
```

## Testes

```bash
pytest --cov=core
```
