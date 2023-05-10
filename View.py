from Controller import *
import tkinter as tk
from model.Cliente import *


class View:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.label1 =tk.Label()
