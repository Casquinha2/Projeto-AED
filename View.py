from Controller import *
import tkinter as tk
from model.ClientLinkedList import*
from model.Cliente import *
from model.UtilizadorTree import *
from tkinter import messagebox
from datetime import datetime
import os


class View:
    def __init__(self, master):
        self.master = master
        self.frame = self.frame_login()
        self.clientes = ClientLinkedList() #Criação da lista de clientes
        self.utilizador = UtilizadorTree(os.chdir("./utilizador"))
        self.root = self.utilizador.get_root()
#        print(self.root.get_left_child())



        
    def frame_login(self):        
        #Frame
        self.master.attributes('-fullscreen', True)
        self.frame = tk.Frame(self.master, bg='#CF0000')
        self.frame.pack()

        #Imagem de fundo
        self.logo2 = tk.PhotoImage(file='teste.png')
        #self.logo = self.logo.subsample(5)
        self.logo_label_desktop = tk.Label(self.master, image=self.logo2)
        #self.logo_label.place(relx=1.0, anchor='ne')
        self.logo_label_desktop.place(relx=.5, rely=.5, anchor= 'center')
        self.logo_label_desktop.lower()

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

        self.registo_button = tk.Button(self.frame, text="Registo  ahaha", font=('Arial', 14), fg='white', bg='#6d7575', command=self.frame_principal)
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
        self.exit_button1 = tk.Button(self.frame1, text="Sair para área de trabalho", font=('Arial', 14), fg='white', bg='#6d7575', command= self.master.destroy)
        self.exit_button1.pack(pady=10, ipadx=20, ipady=5)
        
        #botão de registo de despesas 
        self.registo_despesas_button1 = tk.Button(self.frame1, text="Registar despesas", font=('Arial', 14), fg='white', bg='#6d7575', command= self.frame_registar_despesas)
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
            self.registo_utilizador.tkraise()
        else:
            if nome == '' or password == '':
                messagebox.showerror('Erro.', 'Credênciais inválidas.')
                self.nome_entry3.delete(0, 'end')
                self.password_entry3.delete(0, 'end')
                self.nif_entry3.delete(0, 'end')
                self.registo_utilizador.tkraise()
            else:
                if self.clientes.find_username(nome) == -1:
                    self.clientes.insert_last(cliente)
                    messagebox.showinfo('Sucesso!', 'Usuário registado com sucesso. Já pode fazer o login em sua conta.')
                    self.registo_utilizador.destroy()
                else:
                    messagebox.showerror('Usuário existente.', 'Por favor, digite um nome de usuário que ainda não foi registado.')
                    self.nome_entry3.delete(0, 'end')
                    self.password_entry3.delete(0, 'end')
                    self.nif_entry3.delete(0, 'end')
                    self.registo_utilizador.tkraise()

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
    
    def frame_registar_despesas(self):
        #frame do registo de despesas
        self.registo_despesa = tk.Toplevel(self.master)
        self.registo_despesa.configure(bg= '#CF0000')
        
        #valor de despesa
        self.valor_despesas_label2 = tk.Label(self.registo_despesa, text="Valor da despesa: ", font=('Arial', 14), bg='#CF0000')
        self.valor_despesas_label2.pack()
        self.valor_despesas_entry2 = tk.Entry(self.registo_despesa, font=('Arial', 14),)
        self.valor_despesas_entry2.pack(pady=5)

        #data de despesa
        self.data_despesas_label2 = tk.Label(self.registo_despesa, text="Data da despesa: ", font=('Arial', 14), bg='#CF0000')
        self.data_despesas_label2.pack()
        self.data_despesas_entry2 = tk.Entry(self.registo_despesa, font=('Arial', 14))
        self.data_despesas_entry2.pack(pady=5)
#        self.data = datetime.now()
#        self.formato1 = self.data.strftime("%d/%m/%Y")
        
        #categoria de despesa
        self.categoria_despesas_label2 = tk.Label(self.registo_despesa, text="Categoria da despesa: ", font=('Arial', 14), bg='#CF0000')
        self.categoria_despesas_label2.pack()
        self.categoria_despesas_entry2 = tk.Entry(self.registo_despesa, font=('Arial', 14),)
        self.categoria_despesas_entry2.pack(pady=5)
        
        #descrição de despesa
        self.descrição_despesas_label2 = tk.Label(self.registo_despesa, text="Descrição da despesa (Almoço em restaurante): ", font=('Arial', 14), bg='#CF0000')
        self.descrição_despesas_label2.pack()
        self.descrição_despesas_entry2 = tk.Entry(self.registo_despesa, font=('Arial', 14))
        self.descrição_despesas_entry2.pack(pady=5)

        #Botão de registar despesa
        self.registo_button2 = tk.Button(self.registo_despesa, text="Registo de Despesas", font=('Arial', 14), bg='#6d7575', command=self.caracteristicas_despesas)
        self.registo_button2.pack(pady=10, ipadx=20, ipady=5)

    def valor_despesa(self):
        valor_despesa = self.valor_despesas_entry2.get()
        if valor_despesa != float :
            messagebox.showerror("Erro","Caracter inválido")
            self.valor_despesas_entry2.delete(0,"end")

        else :
            return True
        
    def  categoria_despesas(self):
        categoria_despesas = self.categoria_despesas_entry2.get()
        if categoria_despesas != str :
            messagebox.showerror("Erro","Caracter inválido")
            self.categoria_despesas_entry2.delete(0,'end')
        else :
            return True
        
    def  descrição_despesas(self):
        descrição_despesa = self.descrição_despesas_entry2.get()
        if descrição_despesa != str:
            messagebox.showerror("Erro","Caracter inválido")
            self.descrição_despesas_entry2.delete(0,'end')

        else :
            return True
        
    #caracteristicas das despesas
    def caracteristicas_despesas(self):
        valor_despesas = self.categoria_despesas_entry2.get()
        data_despesas = self.data_despesas_entry2.get()
        categoria_despesas =  self.categoria_despesas_entry2.get()
        descrição_despesa = self.descrição_despesas_entry2.get()
         
        if self. descrição_despesas() == True and self.categoria_despesas() and self.valor_despesa():
            pass
            
            



      

    def frame_registar(self):        
        #Frame
        self.registo_utilizador = tk.Toplevel(self.master, bg='#C90000')
        self.registo_utilizador.geometry('450x300')
        self.registo_utilizador.resizable(False, False)

        #Label + Entry para username
        self.nome_label3 = tk.Label(self.registo_utilizador, text="Nome:", font=('Arial', 14), bg='#C90000')
        self.nome_label3.pack()
        self.nome_entry3 = tk.Entry(self.registo_utilizador, font=('Arial', 14))
        self.nome_entry3.pack(pady=5)

        self.nif_label3 = tk.Label(self.registo_utilizador, text="NIF:", font=('Arial', 14), bg='#C90000')
        self.nif_label3.pack()
        self.nif_entry3 = tk.Entry(self.registo_utilizador, font=('Arial', 14))
        self.nif_entry3.pack(pady=5)     

        #Label + Entry para password
        self.password_label3 = tk.Label(self.registo_utilizador, text="Password:", font=('Arial', 14), bg='#C90000')
        self.password_label3.pack()
        self.password_entry3 = tk.Entry(self.registo_utilizador, show="*", font=('Arial', 14))
        self.password_entry3.pack(pady=5)





#[{nome:..., senha:..., nif:...}, despesas, grafico,....]
#[{nome:..., se, despesas, grafico,...]

#[{nome:..., senha:..., nif:...}, {nome:..., senha:..., nif:...}, {nome:..., senha:..., nif:...}