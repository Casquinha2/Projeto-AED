from Controller import *
import tkinter as tk
class View:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()

    def login(utilizador):
        try:
            ficheiro = ler_ficheiro_json(utilizador)
        except FileNotFoundError:
            print("""
            O utilizador introduzido não tem conta criada.
                Tente novamente ou crie um novo utilizador.
            """)
        else:
            nif = input("Por favor introduza o NIF: ")
            if nif == ficheiro[1]:
                pass
