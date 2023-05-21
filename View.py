from Controller import *
import tkinter as tk
from model.ClientLinkedList import*
from model.Cliente import *
from tkinter import messagebox
from datetime import datetime


class View:
    def __init__(self, master):
        self.master = master
        self.frame = self.frame_login()
        self.clientes = ClientLinkedList() #Criação da lista de clientes
        
    def frame_login(self):        
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

        self.nif_label = tk.Label(self.frame, text="NIF:", font=('Arial', 14), bg='#ffe76c')
        self.nif_label.pack()
        self.nif_entry = tk.Entry(self.frame, font=('Arial', 14))
        self.nif_entry.pack(pady=5)     

        #Label + Entry para password
        self.password_label = tk.Label(self.frame, text="Password:", font=('Arial', 14), bg='#ffe76c')
        self.password_label.pack()
        self.password_entry = tk.Entry(self.frame, show="*", font=('Arial', 14))
        self.password_entry.pack(pady=5)

        #Botões de Login + registo
        self.login_button = tk.Button(self.frame, text="Login", font=('Arial', 14),fg='white', bg='#6d7575', command=self.login)
        self.login_button.pack(pady=10, ipadx=20, ipady=5)

        self.registo_button = tk.Button(self.frame, text="Registo", font=('Arial', 14), fg='white', bg='#6d7575', command=self.registar)
        self.registo_button.pack(pady=10, ipadx=20, ipady=5)

        #botão de fecho do programa
        self.shutdown_button = tk.Button(self.frame, text="Sair", font=('Arial', 14), fg='white', bg='#6d7575', command= self.master.destroy)
        self.shutdown_button.pack(pady=10, ipadx=20, ipady=5)
    
    
    def frame_principal(self):
        #Frame de despesas
        self.master.withdraw()
        self.frame1 = tk.Toplevel(self.master)
        self.frame1.attributes('-fullscreen', True)
        self.frame1.configure(bg= '#ffe76c')
        
        #botão de shutdown ==> ok
        self.shutdown_button2 = tk.Button(self.frame1, text="Sair", font=('Arial', 14), fg='white', bg='#6d7575', command= quit)
        self.shutdown_button2.pack(pady=10, ipadx=20, ipady=5)
        
        #botão de voltar ==> ok
        self.exit_button = tk.Button(self.frame1, text="Sair para área de trabalho", font=('Arial', 14), fg='white', bg='#6d7575', command= self.quit)
        self.exit_button.pack(pady=10, ipadx=20, ipady=5)
        
        #botão de registo de despesas 
        self.registo_despesas_button = tk.Button(self.frame1, text="Registar despesas", font=('Arial', 14), fg='white', bg='#6d7575', command= self.registo_despesas)
        self.registo_despesas_button.pack(pady=10, ipadx=20, ipady=5)
#        messagebox.askquestion('', 'O utilizador ainda não definiu um orçamento mensal. Deseja definir?')

        #botão de detalhes
        self.detalhes_button = tk.Button(self.frame1, text="Ver mais detalhes", font=('Arial', 14), fg='white', bg='#6d7575')
        self.detalhes_button.pack(pady=10, ipadx=20, ipady=5)

        #botão de defição de orçamento mensal
        self.orcamento_button = tk.Button(self.frame1, text="Definir orçamento mensal", font=('Arial', 14), fg='white', bg='#6d7575')
        self.orcamento_button.pack(pady=10, ipadx=20, ipady=5)

    def quit(self):
        self.frame1.destroy()
        self.master.deiconify()

    def registar(self):
        nome = self.nome_entry.get()
        password = self.password_entry.get()
        nif = self.nif_entry.get().strip()
        cliente = Cliente(nome, password, nif)
        try:
            if cliente.controlNIF(nif) == False:
                raise ValueError
        except ValueError:
            messagebox.showerror('Erro.', 'NIF inválido.')
        else:
            if nome == '' or password == '':
                messagebox.showerror('Erro.', 'Credênciais inválidas.')
            else:
                if self.clientes.find_username(nome) == -1:
                    self.clientes.insert_last(cliente)
                    messagebox.showinfo('Sucesso!', 'Usuário registado com sucesso. Já pode fazer o login em sua conta.')
                else:
                    messagebox.showerror('Usuário existente.', 'Por favor, digite um nome de usuário diferente.')

    def login(self):
        if self.clientes.is_empty == True:
            messagebox.showerror('Nenhum usuário registado', 'Por favor, registe um usuário antes de fazer login.')
        else:
            nome = self.nome_entry.get()
            password = self.password_entry.get()
            nif = self.nif_entry.get().strip()
            posicao = self.clientes.find_username(nome)
            if posicao == -1:
                messagebox.showerror('Erro.', 'Credênciais inválidas.')
            else:
                if self.clientes.get(posicao).get_password() != password:
                    messagebox.showerror('Erro.', 'Credênciais inválidas.')
                else:
                    if self.clientes.get(posicao).get_nif() != nif:
                        messagebox.showerror('Erro.', 'Credênciais inválidas.')
                    else:
                        self.frame_principal()                    
    
    def registo_despesas(self):
        #frame do registo de despesas
        self.frame2 = tk.Toplevel(self.master)
        self.frame2.configure(bg= '#ffe76c')
        
        #valor de despesa
        self.valor_despesas_label = tk.Label(self.frame2, text="Valor da despesa: ", font=('Arial', 14), bg='#ffe76c')
        self.valor_despesas_label.pack()
        self.valor_despesas_entry = tk.Entry(self.frame2, font=('Arial', 14))
        self.valor_despesas_entry.pack(pady=5)

        #data de despesa
        self.data_despesas_label = tk.Label(self.frame2, text="Data da despesa: ", font=('Arial', 14), bg='#ffe76c')
        self.data_despesas_label.pack()
        self.data_despesas_entry = tk.Entry(self.frame2, font=('Arial', 14))
        self.data_despesas_entry.pack(pady=5)
#        self.data = datetime.now()
#        self.formato1 = self.data.strftime("%d/%m/%Y")
        
        #categoria de despesa
        self.categoria_despesas_label = tk.Label(self.frame2, text="Categoria da despesa: ", font=('Arial', 14), bg='#ffe76c')
        self.categoria_despesas_label.pack()
        self.categoria_despesas_entry = tk.Entry(self.frame2, font=('Arial', 14))
        self.categoria_despesas_entry.pack(pady=5)
        
        #descrição de despesa
        self.descrição_despesas_label = tk.Label(self.frame2, text="Descrição da despesa (Almoço em restaurante): ", font=('Arial', 14), bg='#ffe76c')
        self.descrição_despesas_label.pack()
        self.descrição_despesas_entry = tk.Entry(self.frame2, font=('Arial', 14))
        self.descrição_despesas_entry.pack(pady=5)


#[{nome:..., senha:..., nif:...}, despesas, grafico,....]
#[{nome:..., se, despesas, grafico,...]

#[{nome:..., senha:..., nif:...}, {nome:..., senha:..., nif:...}, {nome:..., senha:..., nif:...}