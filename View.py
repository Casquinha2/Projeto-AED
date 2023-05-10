from Controller import *
import tkinter as tk
from model.ClientLinkedList import*
from model.Cliente import *
from tkinter import messagebox
class View:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.clientes = ClientLinkedList() #Criação da lista de clientesº
            
        #Frame
        self.master.attributes('-fullscreen', True)
        self.master.configure(bg= '#ffe76c')
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

    def registar(self):
              #Implementar a função registo()

            #Criação de um usuário
            nome = self.nome_entry.get()
            password = self.password_entry.get()            
            cliente = Cliente(nome, password)
            
            if  self.clientes.head is None:
                self.clientes.insert_last(cliente)
                
                messagebox.showinfo('Sucesso!', 'Usuário registado com sucesso. Já pode fazer o login em sua conta.')                    

            else: 
                if self.clientes.head is not None:
                    i = self.clientes.find_username(nome)
                    
                    if i == -1:
                        self.clientes.insert_last(cliente)
                        messagebox.showinfo('Sucesso!', 'Usuário registado com sucesso. Já pode fazer o login em sua conta.')

                    elif self.clientes.get(i).get_nome() == cliente.get_nome():
                        messagebox.showinfo('Usuário existente.', 'Por favor, digite um nome de usuário diferente.')
                        print(self.clientes.size)
                        print(self.clientes.get_first().get_nome())


    def login(self):
        
            
        if self.clientes.size <= 0:
            messagebox.showerror('Nenhum usuário registado', 'Por favor, registe um usuário antes de fazer login.')

        else:
            if self.clientes is not None:
                try:

                    if self.clientes.size > 0:
                        nome = self.nome_entry.get()
                        password = self.password_entry.get()
                        i = self.clientes.find_username(nome)
                        print(nome)
                        print(password) 
                        try:
                            if self.clientes.get(i).get_nome() == nome:
                                if self.clientes.get(i).get_password() == password:
                                    messagebox.showinfo('Sucesso!', 'Usuário logado com sucesso.')
                                    print(self.clientes.get(i).get_nome())
                                    return True

                                else:
                                    messagebox.showerror('Erro.', 'Credênciais inválidas.')
                                              

                        except Exception or AttributeError:
                            messagebox.showerror('Erro de login', 'Usuário não encontrado.')

                except AttributeError:
                    messagebox.showerror('erro de login', 'usuário não encontrado.')