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
        self.orcamento = 0  #depois sai daqui
        self.master = master
        self.frame = self.frame_login()
#        self.despesas = 
        self.clientes = ClientLinkedList() #Criação da lista de clientes
        node = BinaryTreeNode()
        node.set_element("./utilizador")   #Estamos a trabalhar com o nome das pastas e nao com as pastas em si!!!
        self.utilizador = UtilizadorTree(node)
        self.root = self.utilizador.get_root()

        #opcao = Controller().ler_ficheiro_json("utilizador")
        #for i in range (0,len(opcao)):    
        #    self.clientes.insert_last(opcao[i])
        
    def frame_login(self):        
        #Frame
        self.master.attributes('-fullscreen', True)
        self.master.title('Spending Control')
        
        #Imagem de icone
        self.logo3 = tk.PhotoImage(file='ual.png')
        self.master.iconphoto(True, self.logo3)
        
        #bg
        self.bg = tk.PhotoImage(file='fundo5.png')
        self.canvas_test = tk.Canvas(self.master, width= 1920, height= 1080, highlightbackground= 'black')
        self.canvas_test.pack(fill='both', expand= True)
        self.canvas_test.create_image(0, 0, image= self.bg, anchor= 'nw')
        
        #Label + Entry para username
        self.canvas_test.create_text(400, 265, text="Nome: ", font=('Arial', 14), fill='black')
        self.nome_entry = tk.Entry(self.canvas_test, font=('Arial', 14), bg='#d8e6f4')
        self.canvas_test.create_window(400, 290, window= self.nome_entry)

        self.canvas_test.create_text(400, 325, text="NIF:", font=('Arial', 14), fill='black')
        self.nif_entry = tk.Entry(self.canvas_test, font=('Arial', 14), bg='#d8e6f4')
        self.canvas_test.create_window(400, 350, window= self.nif_entry)     

        #Label + Entry para password
        self.canvas_test.create_text(400, 385, text="Password:", font=('Arial', 14), fill='black')
        self.password_entry = tk.Entry(self.canvas_test, show="*", font=('Arial', 14), bg='#d8e6f4')
        self.canvas_test.create_window(400, 410, window= self.password_entry)

        #Botões de Login + registo
        self.login_button = tk.Button(self.canvas_test, text="Login", font=('Arial', 14), command=self.login, bg='#d8e6f4')
        self.canvas_test.create_window(450, 480, anchor='center', window= self.login_button)

        self.registo2_button = tk.Button(self.canvas_test, text="Registo", font=('Arial', 14), command=self.frame_registar, bg='#d8e6f4')
        self.canvas_test.create_window(350, 480, anchor='center', window= self.registo2_button)

        self.registo_button = tk.Button(self.canvas_test, text="Registo  ahaha", font=('Arial', 14), fg='white', bg='#2343b4', command=self.frame_principal)
        self.canvas_test.create_window(1280, 150, anchor='center', window= self.registo_button)

        #botão de fecho do programa
        self.shutdown_button = tk.Button(self.canvas_test, text="Sair", font=('Arial', 14), command= self.master.destroy, bg='#d8e6f4')
        self.canvas_test.create_window(400, 550, anchor='center', window= self.shutdown_button)
        
        # botão ajuda
        self.ajuda_btt = tk.Button(self.canvas_test, text="Ajuda", font=('Arial', 14), command=self.frame_ajuda, bg='#d8e6f4')
        self.canvas_test.create_window(550, 720, anchor='center', window= self.ajuda_btt)

    def frame_principal(self):
        #Frame de despesas
        self.master.withdraw()
        self.frame1 = tk.Toplevel(self.master)
        self.frame1.attributes('-fullscreen', True)

        #bg
        self.bg_2 = tk.PhotoImage(file='teste.png')
        self.canvas_bg_principal = tk.Canvas(self.frame1, width= 1920, height= 1080, highlightbackground= 'black')
        self.canvas_bg_principal.pack(fill='both', expand= True)
        self.canvas_bg_principal.create_image(0, 0, image= self.bg_2, anchor= 'nw')
        
        #botão de voltar ==> ok
        self.shutdown_button1 = tk.Button(self.canvas_bg_principal, text="Log out", font=('Arial', 14), fg='white', bg='#6d7575', command=self.quit)
        self.canvas_bg_principal.create_window(775, 345, anchor='center', window= self.shutdown_button1)
        
        #botão de shutdown ==> ok
        self.exit_button1 = tk.Button(self.canvas_bg_principal, text="Sair para área de trabalho", font=('Arial', 14), fg='white', bg='#6d7575', command= self.master.destroy)
        self.exit_button1.pack(pady=10, ipadx=20, ipady=5)
        
        #botão de registo de despesas 
        self.registo_despesas_button1 = tk.Button(self.canvas_bg_principal, text="Registar despesas", font=('Arial', 14), fg='white', bg='#6d7575', command= self.pergunta_orcamento)
        self.registo_despesas_button1.pack(pady=10, ipadx=20, ipady=5)
        
        #botão de detalhes
        self.detalhes_button1 = tk.Button(self.canvas_bg_principal, text="Ver mais detalhes", font=('Arial', 14), fg='white', bg='#6d7575')
        self.detalhes_button1.pack(pady=10, ipadx=20, ipady=5)

        #botão de defição de orçamento mensal
        self.orcamento_button1 = tk.Button(self.canvas_bg_principal, text="Definir orçamento mensal", font=('Arial', 14), fg='white', bg='#6d7575', command=self.orcamento_mensal)
        self.orcamento_button1.pack(pady=10, ipadx=20, ipady=5)

    def pergunta_orcamento(self):
        if self.orcamento == 0:
            message = messagebox.askquestion('Pergunta.', 'O utilizador ainda não definiu um orçamento mensal. Deseja definir?')
            if message == "yes":
                self.orcamento_mensal()
            else:
                self.frame_registar_despesa()
        else:
            self.frame_registar_despesa()

    def frame_registar_despesa(self):        
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
        #self.categoria_despesas_label2 = tk.Label(self.registo_despesa, text="Categoria da despesa: ", font=('Arial', 14), bg='#CF0000')
        #self.categoria_despesas_label2.pack()
        #self.categoria_despesas_entry2 = tk.Entry(self.registo_despesa, font=('Arial', 14),)
        #self.categoria_despesas_entry2.pack(pady=5)

        self.categoria_despesas_label2 = tk.Label(self.registo_despesa, text="Categoria da despesa: ", font=('Arial', 14), bg='#CF0000')
        self.categoria_despesas_label2.pack()
        self.categoria_despesas_options = ['Selecione uma opção', 'Alimentação', 'Transporte', 'Moradia', 'Lazer', 'Outro'] 
        self.categoria_despesas_var = tk.StringVar(self.registo_despesa)
        self.categoria_despesas_var.set(self.categoria_despesas_options[0])
        self.categoria_despesas_menu = tk.OptionMenu(self.registo_despesa, self.categoria_despesas_var, *self.categoria_despesas_options)
        self.categoria_despesas_menu.config(font=('Arial', 10))
        self.categoria_despesas_menu.pack(pady=5)
        
        #descrição de despesa
        self.descrição_despesas_label2 = tk.Label(self.registo_despesa, text="Descrição da despesa (Almoço em restaurante): ", font=('Arial', 14), bg='#CF0000')
        self.descrição_despesas_label2.pack()
        self.descrição_despesas_entry2 = tk.Entry(self.registo_despesa, font=('Arial', 14))
        self.descrição_despesas_entry2.pack(pady=5)

        #Botão de registar despesa
        self.registo_button2 = tk.Button(self.registo_despesa, text="Registo de Despesas", font=('Arial', 14), bg='#6d7575', command=self.caracteristicas_despesas)
        self.registo_button2.pack(pady=10, ipadx=20, ipady=5)

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
                        self.frame_principal()                    
    
    def quit(self):
        self.master.deiconify()
        self.canvas_bg_principal.destroy()


    #frame de registar utilizador janela pequena
    def frame_registar(self):        
       
        self.registo_utilizador = tk.Toplevel(self.master, bg='#3784e7')
        self.registo_utilizador.geometry('450x300')
        self.registo_utilizador.resizable(False, False)

        #Label + Entry para username
        self.nome_label3 = tk.Label(self.registo_utilizador, text="Nome:", font=('Arial', 14), bg='#3784e7')
        self.nome_label3.pack()
        self.nome_entry3 = tk.Entry(self.registo_utilizador, font=('Arial', 14))
        self.nome_entry3.pack(pady=5)

        self.nif_label3 = tk.Label(self.registo_utilizador, text="NIF:", font=('Arial', 14), bg='#3784e7')
        self.nif_label3.pack()
        self.nif_entry3 = tk.Entry(self.registo_utilizador, font=('Arial', 14))
        self.nif_entry3.pack(pady=5)     

        #Label + Entry para password
        self.password_label3 = tk.Label(self.registo_utilizador, text="Password:", font=('Arial', 14), bg='#3784e7')
        self.password_label3.pack()
        self.password_entry3 = tk.Entry(self.registo_utilizador, show="*", font=('Arial', 14))
        self.password_entry3.pack(pady=5)
        
        self.registo_button1 = tk.Button(self.registo_utilizador, text="Registo de Utilizador", font=('Arial', 14),fg='black', bg='#d8e6f4', command=self.registar)
        self.registo_button1.pack(pady=10, ipadx=20, ipady=5)

        
    #caracteristicas das despesas
    def caracteristicas_despesas(self):
        if self.categoria_despesas_var.get() == "outro":
            pass
            self.outro_categoria()
        elif self.categoria_despesas_var.get() == "Selecione uma opção":
            messagebox.showerror("Erro", "Por favor selecione uma despesa para conseguir prosseguir.")
            return None
        else:
            valor_despesas = Cliente.valor_despesa(self.valor_despesas_entry2.get())
            data_despesas = Cliente.data_despesas(self.data_despesas_entry2.get())
            descrição_despesa = Cliente.descrição_despesas(self.descrição_despesas_entry2.get())
            categoria_despesa = self.categoria_despesas_var.get()
            print(categoria_despesa)
            if valor_despesas != False and data_despesas != False and descrição_despesa != False:
                messagebox.showinfo("Sucesso","Despesa registada ")
                self.registo_despesa.destroy()
            else:
                self.descrição_despesas_entry2.delete(0,'end')
                self.categoria_despesas_var.set(self.categoria_despesas_options[0])
                self.valor_despesas_entry2.delete(0,"end")
                self.data_despesas_entry2.delete(0,'end')
                messagebox.showerror("Erro", "Um dos campos foi mal preenchido.\nPor favor introduza novamente.")

    # pagina de ajuda ao utilizador
    def frame_ajuda(self):
        self.master.withdraw()
        self.ajuda= tk.Toplevel(self.master)
        self.ajuda.attributes('-fullscreen', True)
        self.ajuda.configure(bg= '#CF0000')

        #label para ajudar com os valores de despesa       
        self.valor_despesas_ajuda = tk.Label(self.ajuda, text=" 1- Insira valores do tipo inteiro ou float quando for registar os valores da despesa.", font=('Arial Black', 20), bg='#CF0000', fg='white')
        self.valor_despesas_ajuda.pack()

        # label para ajudar com a data
        self.data_ajuda = tk.Label(self.ajuda, text=" 2- Insira este formato data, (dia/mês/ano), exemplo 25/05/23.", font=('Arial Black', 20), bg='#CF0000', fg='white')
        self.data_ajuda.pack()

        #label para ajudar com as categoria despesas
        self.data_ajuda = tk.Label(self.ajuda, text=" 3- Escolha ou insira a categoria pretendida, caso for inserir a categoria utilize apenas caracteres do tipo str.Exemplo (Alimentacao) .", font=('Arial Black', 20), bg='#CF0000', fg='white')
        self.data_ajuda.pack()
         
    # Botão para voltar para a pagina anteriror
        self.shutdown_ajuda = tk.Button(self.ajuda, text="Voltar", font=('Arial', 14), fg='white', bg='#6d7575', command=self.quit_ajuda)
        self.shutdown_ajuda.pack(pady=10, ipadx=20, ipady=5)

    def quit_ajuda(self):
        self.ajuda.destroy()
        self.master.deiconify()

    def orcamento_mensal(self):

        #frame do orcamento mensal
        self.frame_orc = tk.Toplevel(self.master)
        self.frame_orc.configure(bg= '#CF0000')

        #orcamento mensal
        self.orcamento_label=tk.Label(self.frame_orc, text="Indique o seu orçamento mensal.", font=("Arial", 14), bg="#CF0000")
        self.orcamento_label.pack()
        self.orcamento_entry = tk.Entry(self.frame_orc, font=("Arial", 14))
        self.orcamento_entry.pack(pady = 5)
        self.orcamento_button = tk.Button(self.frame_orc, text = "Confirmar", font=("Arial", 14), bg="#6d7575", command = self.salvar_orcamento)
        self.orcamento_button.pack(pady=5)

    def salvar_orcamento(self):
        try:
            self.orcamento = float(self.orcamento_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "Esse valor não é aceite para o orçamento mensal.\nPor favor tente introduzir um outro valor.")
            self.orcamento_entry.delete("end", 0)
        else:
            messagebox.showinfo("Sucesso", f"O seu orçamento mensal está definido para {self.orcamento}€.")
            self.frame_orc.destroy()

        



#[{nome:..., senha:..., nif:...}, despesas, grafico,....]
#[{nome:..., se, despesas, grafico,...]

#[{nome:..., senha:..., nif:...}, {nome:..., senha:..., nif:...}, {nome:..., senha:..., nif:...}