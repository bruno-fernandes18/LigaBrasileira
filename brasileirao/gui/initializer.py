import tkinter as tk
from .frames.menu_frame import MenuFrame

def _enforce_ratio(event: tk.Event):
    root = event.widget
    if getattr(root, "_ratio_lock", False):
        return
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
    root.geometry(f"{w}x{h}")
    root._ratio_lock = False

def start(root: tk.Tk):
    root.title("Liga Brasileira")
    root.geometry("1280x720")
    root.minsize(1280, 720)
    root.bind("<Configure>", _enforce_ratio)
    MenuFrame(root).pack(fill="both", expand=True)
