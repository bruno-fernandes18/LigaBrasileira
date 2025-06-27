import tkinter as tk
from brasileirao.gui import initializer

class App:
    def __init__(self):
        self.root = tk.Tk()
        initializer.start(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    App().run()
