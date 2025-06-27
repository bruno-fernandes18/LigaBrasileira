import tkinter as tk
from .frames.menu_frame import MenuFrame

def start(root: tk.Tk):
    root.title("Liga Brasileira")
    MenuFrame(root).pack(fill='both', expand=True)
