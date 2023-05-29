import tkinter as tk
from model.ClientLinkedList import*
from model.Cliente import *
from model.Despesas import *
from model.DespesasLinkedList import *
from tkinter import messagebox
from datetime import datetime
from model.Ficheiro import *
from model.Categoria import*
from model.CategoriaLinkedList import*
from tkcalendar import DateEntry


class View:
    def __init__(self, master):
        self.ficheiro = Ficheiro
        self.master = master
        self.frame = self.frame_login()
        self.clientes = ClientLinkedList()
        self.clientes = self.ficheiro.json_para_linkedlist_cliente(self.clientes)
        self.despesas = DespesaslinkedList()


        
    def frame_login(self):        
        #Frame
        self.master.attributes('-fullscreen', True)
        self.master.title('Spending Control')
        
        #Imagem de icone
        self.logo3 = tk.PhotoImage(file='imagens/ual.png')
        self.master.iconphoto(True, self.logo3)
        
        #bg
        self.bg = tk.PhotoImage(file='imagens/fundo5.png')
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
        self.ajuda_btt = tk.Button(self.canvas_test, text="Ajuda", font=('Arial', 14), command=self.messagebox_ajuda_login, bg='#d8e6f4')
        self.canvas_test.create_window(550, 720, anchor='center', window= self.ajuda_btt)

    def frame_principal(self):
        #Frame de despesas
        self.master.withdraw()
        
        self.frame1 = tk.Toplevel(self.master, bg= 'black')
        self.frame1.attributes('-fullscreen', True)
        
        #bg
        self.canvas_bg_principal= tk.Canvas(self.frame1, width= 500, height= 350, background= '#4DB6E5', highlightbackground='#4DB6E5')
        self.canvas_bg_principal.pack(fill='both', expand= True)
        self.canvas_bg_principal.create_rectangle(900, 500, 1475, 825, fill= '#92C3EC')
        self.canvas_bg_principal.create_rectangle(50, 50, 1500, 450, fill= 'white')
        
        #botão logout ==> ok
        self.shutdown_button1 = tk.Button(self.canvas_bg_principal, text="Log out", font=('Arial', 16), fg='black', bg='#92C3EC', command=self.quit)
        self.canvas_bg_principal.create_window(1070, 715, anchor='center', window= self.shutdown_button1)
        
        #botão de shutdown ==> ok
        self.exit_button1 = tk.Button(self.canvas_bg_principal, text="Sair para área de trabalho", font=('Arial', 16), fg='black', bg='#92C3EC', command= self.master.destroy)
        self.canvas_bg_principal.create_window(1190, 780, anchor='center', window= self.exit_button1)
        
        #botão de registo de despesas 
        self.registo_despesas_button1 = tk.Button(self.canvas_bg_principal, text="Registar despesas", font=('Arial', 16), fg='black', bg='#92C3EC', command= self.pergunta_orcamento)
        self.canvas_bg_principal.create_window(1075, 635, anchor='center', window= self.registo_despesas_button1)
        
        #botão de sugestoes
        self.detalhes_button1 = tk.Button(self.canvas_bg_principal, text="Sugestões de cortes", font=('Arial', 16), fg='black', bg='#92C3EC', command=self.sugestoes)
        self.canvas_bg_principal.create_window(1330, 635, anchor='center', window= self.detalhes_button1)

        #botão de defição de orçamento mensal
        self.orcamento_button1 = tk.Button(self.canvas_bg_principal, text="Definir orçamento mensal", font=('Arial', 16), fg='black', bg='#92C3EC', command=self.orcamento_mensal)
        self.canvas_bg_principal.create_window(1190, 560, anchor='center', window= self.orcamento_button1)
        
        #botão de ajuda ==> ok
        self.exit_button1 = tk.Button(self.canvas_bg_principal, text="Ajuda", font=('Arial', 16), fg='black', bg='#92C3EC', command= self.messagebox_ajuda_despesas)
        self.canvas_bg_principal.create_window(1310, 715, anchor='center', window= self.exit_button1)

    def pergunta_orcamento(self):
        if self.orcamento == 0:
            message = messagebox.askquestion('Pergunta.', 'O utilizador ainda não definiu um orçamento mensal, nem um limite mensal. Deseja definir?')
            if message == "yes":
                self.orcamento_mensal()
            else:
                self.frame_registar_despesa()
        else:
            self.frame_registar_despesa()

    def frame_registar_despesa(self):        
        #frame do registo de despesas
        self.registo_despesa = tk.Toplevel(self.master)
        self.registo_despesa.configure(bg= '#4db6e5')
        
        #valor de despesa
        self.valor_despesas_label2 = tk.Label(self.registo_despesa, text="Valor da despesa: ", font=('Arial', 14), bg='#4db6e5')
        self.valor_despesas_label2.pack()
        self.valor_despesas_entry2 = tk.Entry(self.registo_despesa, font=('Arial', 14),  bg='#d8e6f4')
        self.valor_despesas_entry2.pack(pady=5)

        #data de despesa
        self.data_despesas_label2 = tk.Label(self.registo_despesa, text="Data da despesa: ", font=('Arial', 14), bg='#4db6e5')
        self.data_despesas_label2.pack()
        self.data_despesas_entry2 = DateEntry(self.registo_despesa, font=('Arial', 14), bg='#d8e6f4', date_pattern='dd/mm/yyyy', foreground='black', background='#d8e6f4')
        self.data_despesas_entry2.pack(pady=5)


        
        #categoria da despesa
        self.categoria_despesas_label2 = tk.Label(self.registo_despesa, text="Categoria da despesa: ", font=('Arial', 14), bg='#4db6e5')
        self.categoria_despesas_label2.pack()
        self.categoria_despesas_options = ['Selecione uma opção', 'Alimentação', 'Transporte', 'Moradia', 'Lazer', 'Outra'] 
        self.categoria_despesas_var = tk.StringVar(self.registo_despesa)
        self.categoria_despesas_var.set(self.categoria_despesas_options[0])
        self.categoria_despesas_menu = tk.OptionMenu(self.registo_despesa, self.categoria_despesas_var, *self.categoria_despesas_options)
        self.categoria_despesas_menu.config(font=('Arial', 10),  bg='#d8e6f4')
        self.categoria_despesas_menu.pack(pady=5)
        
        #descrição de despesa
        self.descrição_despesas_label2 = tk.Label(self.registo_despesa, text="Descrição da despesa (ex.: Almoço em restaurante): ", font=('Arial', 14), bg='#4db6e5')
        self.descrição_despesas_label2.pack()
        self.descrição_despesas_entry2 = tk.Entry(self.registo_despesa, font=('Arial', 14),  bg='#d8e6f4')
        self.descrição_despesas_entry2.pack(pady=5)

        #Botão de registar despesa
        self.registo_button2 = tk.Button(self.registo_despesa, text="Registo de Despesas", font=('Arial', 14), bg='#d8e6f4', command=self.caracteristicas_despesas)
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
            messagebox.showerror('Erro.', 'Credênciais inválidas.')
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
                if self.clientes.find_username(nome) == -1 and self.clientes.find_nif(nif) == -1:
                    self.clientes.insert_last(cliente)
                    self.ficheiro.linkedlist_para_json_cliente(self.clientes, self.clientes.size)
                    self.ficheiro.linkedlist_para_json_despesa(nome, 0,0, self.despesas)
                    messagebox.showinfo('Sucesso!', 'Usuário registado com sucesso.\nJá pode fazer o login em sua conta.')
                    self.registo_utilizador.destroy()
                    
                else:
                    messagebox.showerror('Erro.', 'Usuário ou NIF existente.\nPor favor, digite um nome de usuário ou um NIF que ainda não foi registado.')
                    self.nome_entry3.delete(0, 'end')
                    self.password_entry3.delete(0, 'end')
                    self.nif_entry3.delete(0, 'end')
                    self.registo_utilizador.tkraise()

    def login(self):
        if self.clientes.is_empty == True:
            messagebox.showerror('Erro', 'Nenhum usuário registado.\nPor favor, registe um utilizador antes de fazer login.')
        else:
            self.nome = self.nome_entry.get()
            password = self.password_entry.get()
            nif = self.nif_entry.get()
            posicao = self.clientes.find_username(self.nome)
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
                        self.orcamento, self.limite, self.despesas = self.ficheiro.json_para_linkedlist_despesa(self.nome)
                        self.nome_entry.delete(0, 'end')
                        self.password_entry.delete(0, 'end')
                        self.nif_entry.delete(0, 'end')
                        self.frame_principal()
                        

    
    def quit(self):
        #self.ficheiro.linkedlist_para_json_despesa(self.nome, self.orcamento, self.despesas)
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
        if self.categoria_despesas_var.get() == "Selecione uma opção":
            messagebox.showerror("Erro", "Por favor selecione uma despesa para conseguir prosseguir.")
            self.categoria_despesas_var.set(self.categoria_despesas_options[0])
        else:
            valor_despesas = Cliente.valor_despesa(self.valor_despesas_entry2.get())
            data_despesas = self.data_despesas_entry2.get()
            descrição_despesa = Cliente.descrição_despesas(self.descrição_despesas_entry2.get())
            categoria_despesa = self.categoria_despesas_var.get()
            if valor_despesas != False and descrição_despesa != False:
                if  Despesa.despesa_valida(valor_despesas, self.despesas, self.orcamento) == True:
                    teste = messagebox.showinfo("Sucesso","Despesa registada ")
                    despesa = Despesa(valor_despesas, data_despesas, descrição_despesa, categoria_despesa)
                    self.despesas.insert_last(despesa)
                    self.ficheiro.linkedlist_para_json_despesa(self.nome, self.orcamento, self.limite, self.despesas)
                    if Despesa.verificar_limite(self.limite, valor_despesas, self.despesas, self.orcamento) == True:
                        self.registo_despesa.destroy()
                    else:
                        self.descrição_despesas_entry2.delete(0,'end')
                        self.categoria_despesas_var.set(self.categoria_despesas_options[0])
                        self.valor_despesas_entry2.delete(0,"end")
                        self.registo_despesa.destroy()
                        messagebox.showwarning("Cuidado", "O seu limite está a ser excedido.")
                        
                else:
                    messagebox.showerror("Erro", "Não é possível introduzir essa despesa pois passará o seu orçamento mensal.")
                    self.registo_despesa.destroy()
            else:
                self.descrição_despesas_entry2.delete(0,'end')
                self.categoria_despesas_var.set(self.categoria_despesas_options[0])
                self.valor_despesas_entry2.delete(0,"end")
                messagebox.showerror("Erro", "Um dos campos foi mal preenchido.\nPor favor introduza novamente.")

    # pagina de ajuda ao utilizador
    def messagebox_ajuda_login(self):
        messagebox.showinfo('Como faço o login?', '''    Caso ainda não tenha efetuado o registo, carregue no botão  "Registo" e preencha os dados. Verifique se o nif esta de acordo com o seu CC (cartão de cidadão).
    Após ter efetuado o registo, preencha os dados do login com os mesmos dados que preencheu quando fez no registo.''')
    
    #pagina de ajuda no registo de despesas
    def messagebox_ajuda_despesas(self):

        #este botao ou deve falar de todas as opcoes na tela principal, ou deve estar na frame de registar despesa
        messagebox.showinfo('Como fazer registo do seus gastos?','''Para registar as suas despesas deve seguir os seguintes passos:
    1º passo: Carregue no botão de registar despesas;
    2º passo: Preencha os dados descritos na nova janela aberta, repare que, na "data da despesa" é necessário escrever a data no seguinte formato (dia/mês/ano);
    3º passo: Após tudo preenchido, carregue em registar despesa e pronto! Seu registo de despesa terá sido feito com sucesso''')

    def orcamento_mensal(self):
        #frame do orcamento mensal
        self.frame_orc = tk.Toplevel(self.master)
        self.frame_orc.configure(bg= '#4db6e5')

        #orcamento mensal
        self.orcamento_label=tk.Label(self.frame_orc, text="Indique o seu orçamento mensal.", font=("Arial", 14), bg="#4db6e5")
        self.orcamento_label.pack()
        self.orcamento_entry = tk.Entry(self.frame_orc, font=("Arial", 14),  bg='#d8e6f4')
        self.orcamento_entry.pack(pady = 5)
        
        #limite mensal
        self.limite_label = tk.Label(self.frame_orc, text=" Defina o valor do limite mensal que pretende o envio da mensagem de alerta ?(Valor em percentagem)", font=("Arial", 14), bg="#4db6e5")
        self.limite_label.pack()
        self.limite_entry = tk.Entry(self.frame_orc, font=("Arial", 14),  bg='#d8e6f4')
        self.limite_entry.pack(pady= 5)

        #Botao confirmar
        self.orcamento_button = tk.Button(self.frame_orc, text = "Confirmar", font=("Arial", 14),  bg='#d8e6f4', command = self.salvar_orcamento)
        self.orcamento_button.pack(pady=5)

    def salvar_orcamento(self):
        try:
            self.orcamento = float(self.orcamento_entry.get())
            self.limite = float(self.limite_entry.get())
            if self.limite < 0 or self.limite > 100:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Esse valor não é aceite para o orçamento mensal ou para o limite mensal.\nPor favor tente introduzir um outro valor.")
            self.orcamento_entry.delete("end", 0)
            self.limite_entry.delete("end", 0)
        else:
            messagebox.showinfo("Sucesso", f"O seu orçamento mensal está definido para {self.orcamento}€.\nE o seu limite mensal é de {self.limite}%.")
            self.frame_orc.destroy()
            self.frame_registar_despesa()

    def sugestoes(self):
        listacategoria = CategorialinkedList()
        alimentacao = transporte = moradia = lazer = outra = 0
        alimentacaova = 0
        transporteva = 0
        moradiava = 0
        lazerva = 0
        outrava = 0
        for i in range(self.despesas.size):
            categoria = self.despesas.get(i).get_categoria()
            if categoria == "Alimenta\u00e7\u00e3o":
                alimentacao += 1
                alimentacaova += self.despesas.get(i).get_valor()
            elif categoria == "Transporte":
                transporte += 1
                transporteva += self.despesas.get(i).get_valor()
            elif categoria == "Moradia":
                moradia += 1
                moradiava += self.despesas.get(i).get_valor()
            elif categoria == "Lazer":
                lazer += 1
                lazerva += self.despesas.get(i).get_valor()
            else:
                outra += 1
                outrava += self.despesas.get(i).get_valor()
        try:
            mediaal = alimentacaova/alimentacao
        except ZeroDivisionError:
            categoriaal = Categoria("Alimenta\u00e7\u00e3o", 0)
        else:
            categoriaal = Categoria("Alimenta\u00e7\u00e3o", mediaal)
        try:
            mediatra = transporteva/transporte
        except ZeroDivisionError:
            categoriatra = Categoria("Transporte",0)
        else:
            categoriatra = Categoria("Transporte",mediatra)
        try:
            mediamo = moradiava/moradia
        except ZeroDivisionError:
            categoriamo = Categoria("Moradia", 0)
        else:
            categoriamo = Categoria("Moradia", mediamo)
        try:
            medialaz = lazerva/lazer
        except ZeroDivisionError:
            categorialaz = Categoria("Lazer", 0)
        else:
            categorialaz = Categoria("Lazer", medialaz)
        try:
            mediaou = outrava/outra
        except ZeroDivisionError:
            categoriaou = Categoria("Outro", 0)
        else:
            categoriaou = Categoria("Outro", mediaou)  
        listacategoria.insert_last(categoriaal)
        listacategoria.insert_last(categoriatra)
        listacategoria.insert_last(categoriamo)
        listacategoria.insert_last(categorialaz)
        listacategoria.insert_last(categoriaou)

        #sort lista

        messagebox.showinfo("Sugestão",f"Anda a gastar mais dinheiro em {listacategoria.get_last().get_categoria()}.\nRecomendamos que corte em algumas dessas despesas.")