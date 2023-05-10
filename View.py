from Controller import *
import tkinter as tk
from model.ClientLinkedList import*
class View:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.clientes = ClientLinkedList() #Criação da lista de clientesº
            
        #Frame
        self.master.attributes('-fullscreen', True)
        self.frame = tk.Frame(self.master, bg='#ffe76c')
        self.frame.pack()

        #Imagem
#        self.logo = tk.PhotoImage(file='movies.png')
#        self.logo = self.logo.subsample(5)
#        self.logo_label = tk.Label(self.frame, image=self.logo, bg='#ffe76c')
#        self.logo_label.place(relx=1.0, anchor='ne')
#        self.logo_label.pack()

        #Label + Entry para username
        self.nome_label = tk.Label(self.frame, text="Nome:", font=('Arial', 14), bg='#ffe76c')
        self.nome_label.pack()
        self.nome_entry = tk.Entry(self.frame, font=('Arial', 14))
        self.nome_entry.pack(pady=5)

        self.nif_label = tk.Label(self.frame, text="Nif:", font=('Arial', 14), bg='#ffe76c')
        self.nif_label.pack()
        self.nif_entry = tk.Entry(self.frame, font=('Arial', 14))
        self.nif_entry.pack(pady=5)     

        #Label + Entry para password
        self.password_label = tk.Label(self.frame, text="Password:", font=('Arial', 14), bg='#ffe76c')
        self.password_label.pack()
        self.password_entry = tk.Entry(self.frame, show="*", font=('Arial', 14))
        self.password_entry.pack(pady=5)

        #Botões de Login + registo
        self.login_button = tk.Button(self.frame, text="Login", font=('Arial', 14),fg='white', bg='#6d7575')
        self.login_button.pack(pady=10, ipadx=20, ipady=5)

        self.registo_button = tk.Button(self.frame, text="Registo", font=('Arial', 14), fg='white', bg='#6d7575')
        self.registo_button.pack(pady=10, ipadx=20, ipady=5)

        #botão de fecho do programa
        self.shutdown_button = tk.Button(self.frame, text="Sair", font=('Arial', 14), fg='white', bg='#6d7575', command= self.master.destroy)
        self.shutdown_button.pack(pady=10, ipadx=20, ipady=5)

