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
        self.master.configure(bg= '#CF0000')
        self.frame = tk.Frame(self.master, bg='#CF0000')
        self.frame.pack()

        #Imagem
#        self.logo = tk.PhotoImage(file='movies.png')
#        self.logo = self.logo.subsample(5)
#        self.logo_label = tk.Label(self.frame, image=self.logo, bg='#CF0000')
#        self.logo_label.place(relx=1.0, anchor='ne')
#        self.logo_label.pack()

        #Label + Entry para username
        self.nome_label = tk.Label(self.frame, text="Nome:", font=('Arial', 14), bg='#CF0000')
        self.nome_label.pack()
        self.nome_entry = tk.Entry(self.frame, font=('Arial', 14))
        self.nome_entry.pack(pady=5)

        self.nif_label = tk.Label(self.frame, text="NIF:", font=('Arial', 14), bg='#CF0000')
        self.nif_label.pack()
        self.nif_entry = tk.Entry(self.frame, font=('Arial', 14))
        self.nif_entry.pack(pady=5)     

        #Label + Entry para password
        self.password_label = tk.Label(self.frame, text="Password:", font=('Arial', 14), bg='#CF0000')
        self.password_label.pack()
        self.password_entry = tk.Entry(self.frame, show="*", font=('Arial', 14))
        self.password_entry.pack(pady=5)

        #Botões de Login + registo
        self.login_button = tk.Button(self.frame, text="Login", font=('Arial', 14),fg='white', bg='#6d7575', command=self.login)
        self.login_button.pack(pady=10, ipadx=20, ipady=5)

        self.registo_button = tk.Button(self.frame, text="Registo", font=('Arial', 14), fg='white', bg='#6d7575', command=self.frame_registar)
        self.registo_button.pack(pady=10, ipadx=20, ipady=5)

        #botão de fecho do programa
        self.shutdown_button = tk.Button(self.frame, text="Sair", font=('Arial', 14), fg='white', bg='#6d7575', command= self.master.destroy)
        self.shutdown_button.pack(pady=10, ipadx=20, ipady=5)
    
    
    def frame_principal(self):
        #Frame de despesas
        self.master.withdraw()
        self.frame1 = tk.Toplevel(self.master)
        self.frame1.attributes('-fullscreen', True)
        self.frame1.configure(bg= '#CF0000')
        
        #botão de shutdown ==> ok
        self.shutdown_button1 = tk.Button(self.frame1, text="Sair", font=('Arial', 14), fg='white', bg='#6d7575', command=quit)
        self.shutdown_button1.pack(pady=10, ipadx=20, ipady=5)
        
        #botão de voltar ==> ok
        self.exit_button1 = tk.Button(self.frame1, text="Sair para área de trabalho", font=('Arial', 14), fg='white', bg='#6d7575', command= self.quit)
        self.exit_button1.pack(pady=10, ipadx=20, ipady=5)
        
        #botão de registo de despesas 
        self.registo_despesas_button1 = tk.Button(self.frame1, text="Registar despesas", font=('Arial', 14), fg='white', bg='#6d7575', command= self.frame_registo_despesas)
        self.registo_despesas_button1.pack(pady=10, ipadx=20, ipady=5)
#        messagebox.askquestion('', 'O utilizador ainda não definiu um orçamento mensal. Deseja definir?')

        #botão de detalhes
        self.detalhes_button1 = tk.Button(self.frame1, text="Ver mais detalhes", font=('Arial', 14), fg='white', bg='#6d7575')
        self.detalhes_button1.pack(pady=10, ipadx=20, ipady=5)

        #botão de defição de orçamento mensal
        self.orcamento_button1 = tk.Button(self.frame1, text="Definir orçamento mensal", font=('Arial', 14), fg='white', bg='#6d7575')
        self.orcamento_button1.pack(pady=10, ipadx=20, ipady=5)

    def quit(self):
        self.frame1.destroy()
        self.master.deiconify()

    def registar(self):
        nome = self.nome_entry3.get()
        password = self.password_entry3.get()
        nif = self.nif_entry3.get()
        cliente = Cliente(nome, password, nif)
        try:
            if cliente.controlNIF(nif) == False:
                raise ValueError
        except ValueError:
            messagebox.showerror('Erro.', 'NIF inválido.')
            self.nome_entry3.delete(0, 'end')
            self.password_entry3.delete(0, 'end')
            self.nif_entry3.delete(0, 'end')
            self.frame3.tkraise()
        else:
            if nome == '' or password == '':
                messagebox.showerror('Erro.', 'Credênciais inválidas.')
                self.nome_entry3.delete(0, 'end')
                self.password_entry3.delete(0, 'end')
                self.nif_entry3.delete(0, 'end')
                self.frame3.tkraise()
            else:
                if self.clientes.find_username(nome) == -1:
                    self.clientes.insert_last(cliente)
                    messagebox.showinfo('Sucesso!', 'Usuário registado com sucesso. Já pode fazer o login em sua conta.')
                    self.frame3.destroy()
                else:
                    messagebox.showerror('Usuário existente.', 'Por favor, digite um nome de usuário que ainda não foi registado.')
                    self.nome_entry3.delete(0, 'end')
                    self.password_entry3.delete(0, 'end')
                    self.nif_entry3.delete(0, 'end')
                    self.frame3.tkraise()

    def login(self):
        if self.clientes.is_empty == True:
            messagebox.showerror('Nenhum usuário registado', 'Por favor, registe um usuário antes de fazer login.')
        else:
            nome = self.nome_entry.get()
            password = self.password_entry.get()
            nif = self.nif_entry.get()
            posicao = self.clientes.find_username(nome)
            if posicao == -1:
                messagebox.showerror('Erro.', 'Credênciais inválidas.')
                self.nome_entry.delete(0, 'end')
                self.password_entry.delete(0, 'end')
                self.nif_entry.delete(0, 'end')
            else:
                if self.clientes.get(posicao).get_password() != password:
                    messagebox.showerror('Erro.', 'Credênciais inválidas.')
                    self.nome_entry.delete(0, 'end')
                    self.password_entry.delete(0, 'end')
                    self.nif_entry.delete(0, 'end')
                else:
                    if self.clientes.get(posicao).get_nif() != nif:
                        messagebox.showerror('Erro.', 'Credênciais inválidas.')
                        self.nome_entry.delete(0, 'end')
                        self.password_entry.delete(0, 'end')
                        self.nif_entry.delete(0, 'end')
                    else:
                        print('teste')
                        self.frame_principal()                    
    
    def frame_registo_despesas(self):
        #frame do registo de despesas
        self.frame2 = tk.Toplevel(self.master)
        self.frame2.configure(bg= '#CF0000')
        
        #valor de despesa
        self.valor_despesas_label2 = tk.Label(self.frame2, text="Valor da despesa: ", font=('Arial', 14), bg='#CF0000')
        self.valor_despesas_label2.pack()
        self.valor_despesas_entry2 = tk.Entry(self.frame2, font=('Arial', 14))
        self.valor_despesas_entry2.pack(pady=5)

        #data de despesa
        self.data_despesas_label2 = tk.Label(self.frame2, text="Data da despesa: ", font=('Arial', 14), bg='#CF0000')
        self.data_despesas_label2.pack()
        self.data_despesas_entry2 = tk.Entry(self.frame2, font=('Arial', 14))
        self.data_despesas_entry2.pack(pady=5)
#        self.data = datetime.now()
#        self.formato1 = self.data.strftime("%d/%m/%Y")
        
        #categoria de despesa
        self.categoria_despesas_label2 = tk.Label(self.frame2, text="Categoria da despesa: ", font=('Arial', 14), bg='#CF0000')
        self.categoria_despesas_label2.pack()
        self.categoria_despesas_entry2 = tk.Entry(self.frame2, font=('Arial', 14))
        self.categoria_despesas_entry2.pack(pady=5)
        
        #descrição de despesa
        self.descrição_despesas_label2 = tk.Label(self.frame2, text="Descrição da despesa (Almoço em restaurante): ", font=('Arial', 14), bg='#CF0000')
        self.descrição_despesas_label2.pack()
        self.descrição_despesas_entry2 = tk.Entry(self.frame2, font=('Arial', 14))
        self.descrição_despesas_entry2.pack(pady=5)

    def frame_registar(self):        
        #Frame
        self.frame3 = tk.Toplevel(self.master, bg='#C90000')
        self.frame3.geometry('450x300')
        self.frame3.resizable(False, False)

        #Label + Entry para username
        self.nome_label3 = tk.Label(self.frame3, text="Nome:", font=('Arial', 14), bg='#C90000')
        self.nome_label3.pack()
        self.nome_entry3 = tk.Entry(self.frame3, font=('Arial', 14))
        self.nome_entry3.pack(pady=5)

        self.nif_label3 = tk.Label(self.frame3, text="NIF:", font=('Arial', 14), bg='#C90000')
        self.nif_label3.pack()
        self.nif_entry3 = tk.Entry(self.frame3, font=('Arial', 14))
        self.nif_entry3.pack(pady=5)     

        #Label + Entry para password
        self.password_label3 = tk.Label(self.frame3, text="Password:", font=('Arial', 14), bg='#C90000')
        self.password_label3.pack()
        self.password_entry3 = tk.Entry(self.frame3, show="*", font=('Arial', 14))
        self.password_entry3.pack(pady=5)

        #Botão de registo
        self.registo_button3 = tk.Button(self.frame3, text="Registo", font=('Arial', 14), fg='white', bg='#6d7575', command=self.registar)
        self.registo_button3.pack(pady=10, ipadx=20, ipady=5)



#[{nome:..., senha:..., nif:...}, despesas, grafico,....]
#[{nome:..., se, despesas, grafico,...]

#[{nome:..., senha:..., nif:...}, {nome:..., senha:..., nif:...}, {nome:..., senha:..., nif:...}