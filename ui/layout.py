import tkinter as tk
from ui.widgets import setup_widgets

def start_app():
    root = tk.Tk()
    root.title("To-Do List App")
    root.geometry("400x500")

    setup_widgets(root)

    root.mainloop()