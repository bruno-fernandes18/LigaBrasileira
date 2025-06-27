"""Inicialização da interface gráfica."""

import logging
import time
import tkinter as tk

from .frames.menu_frame import MenuFrame
from .controller import AppController

logger = logging.getLogger(__name__)


def throttle(delay: float):
    """Decorator to throttle calls to a function."""

    def decorator(fn):
        last_called = 0.0

        def wrapper(*args, **kwargs):
            nonlocal last_called
            now = time.time()
            if now - last_called > delay:
                last_called = now
                return fn(*args, **kwargs)

        return wrapper

    return decorator

@throttle(0.5)
def _enforce_ratio(event: tk.Event) -> None:
    """Force 16:9 ratio for the top level window.

    Args:
        event: Evento de redimensionamento da janela.
    """

    widget = event.widget.winfo_toplevel()
    if not isinstance(widget, tk.Tk):
        logger.warning("Widget %s não suporta geometry", type(widget))
        return
    if not getattr(widget, "is_main_window", False):
        return

    ratio_lock_supported = hasattr(widget, "__dict__")
    if ratio_lock_supported and getattr(widget, "_ratio_lock", False):
        return
    if ratio_lock_supported:
        widget._ratio_lock = True

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

    widget.geometry(f"{w}x{h}")

    if ratio_lock_supported:
        widget._ratio_lock = False

def start(root: tk.Tk) -> None:
    """Configura a janela principal e exibe o menu."""

    root.title("Liga Brasileira")
    root.geometry("1280x720")
    root.minsize(1280, 720)
    root.is_main_window = True
    root.bind("<Configure>", _enforce_ratio)
    controller = AppController()
    MenuFrame(root, controller).pack(fill="both", expand=True)
