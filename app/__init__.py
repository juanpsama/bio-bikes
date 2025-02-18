from tkinter import Tk
from .controller import Controller 

def run_app():
    root = Tk()
    root.title("Análisis Biomecánico")
    root.geometry("500x500")
    root.resizable(False, False)
    Controller(root)
    root.mainloop()