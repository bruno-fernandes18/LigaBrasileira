"""Registro simples de narra\u00e7\u00e3o de partidas."""

from __future__ import annotations

from ..entities.partida import Partida


def narrar(texto: str, partida: Partida) -> None:
    """Adiciona ``texto`` ao hist\u00f3rico de eventos da ``partida``."""
    partida.eventos.append(texto)
