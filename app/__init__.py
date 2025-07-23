from tkinter import Tk
from .controller import Controller 

def run_app():
    root = Tk()
    root.title("Análisis Biomecánico")
    root.resizable(False, True)
    Controller(root)
    root.mainloop()