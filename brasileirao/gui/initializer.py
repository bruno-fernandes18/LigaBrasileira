"""Inicialização da interface gráfica."""

import logging
import tkinter as tk

from .frames.menu_frame import MenuFrame

logger = logging.getLogger(__name__)

def _enforce_ratio(event: tk.Event) -> None:
    """Force 16:9 ratio for the top level window.

    Args:
        event: Evento de redimensionamento da janela.
    """

    root = event.widget.winfo_toplevel()
    ratio_lock_supported = hasattr(root, "__dict__")
    if ratio_lock_supported and getattr(root, "_ratio_lock", False):
        return
    if ratio_lock_supported:
        root._ratio_lock = True

    desired = 16 / 9
    w, h = event.width, event.height
    if w / h > desired:
        w = int(h * desired)
    else:
        h = int(w / desired)

    if w < 1280:
        w = 1280
        h = int(w / desired)
    if h < 720:
        h = 720
        w = int(h * desired)

    if hasattr(root, "geometry"):
        root.geometry(f"{w}x{h}")
    else:
        logger.warning("Widget %s não suporta geometry", type(event.widget))

    if ratio_lock_supported:
        root._ratio_lock = False

def start(root: tk.Tk) -> None:
    """Configura a janela principal e exibe o menu."""

    root.title("Liga Brasileira")
    root.geometry("1280x720")
    root.minsize(1280, 720)
    root.bind("<Configure>", _enforce_ratio)
    MenuFrame(root).pack(fill="both", expand=True)
