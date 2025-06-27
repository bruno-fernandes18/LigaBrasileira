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
    """Mantém a janela principal na proporção 16:9 de forma DPI-aware.

    A função ignora eventos de widgets que não são a janela principal e
    trata possíveis erros ao consultar informações de DPI.

    Args:
        event: Evento gerado pelo redimensionamento.
    """

    if not hasattr(event.widget, "winfo_toplevel"):
        return
    widget = event.widget.winfo_toplevel()
    if not isinstance(widget, (tk.Tk, tk.Toplevel)):
        logger.warning("Widget %s não suporta geometry", type(widget))
        return
    if not getattr(widget, "is_main_window", False):
        return

    try:
        dpi = widget.winfo_fpixels("1i")
        scale = dpi / 72.0
    except (tk.TclError, ValueError):  # pragma: no cover - dependente do SO
        scale = 1.0

    ratio_lock_supported = hasattr(widget, "__dict__")
    if ratio_lock_supported and getattr(widget, "_ratio_lock", False):
        return
    if ratio_lock_supported:
        widget._ratio_lock = True

    desired = 16 / 9
    min_w = int(1280 * scale)
    min_h = int(720 * scale)
    w = max(event.width, min_w)
    h = max(int(w / desired), event.height)
    if h < min_h:
        h = min_h
        w = int(h * desired)

    try:
        widget.geometry(f"{w}x{h}")
    except tk.TclError as exc:  # pragma: no cover - não ocorre em testes
        logger.error("Redimensionamento falhou: %s", exc)
    finally:
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
