import json
from model.DespesasLinkedList import *
from model.Despesas import *
from model.Cliente import *
from model.ClientLinkedList import *

class Ficheiro:
    def escrever_ficheiro_json(self, nome, d):
        json_string = json.dumps(d)
        json_file = open(nome, 'w')
        json_file.write(json_string)
        json_file.close()

    def ler_ficheiro_json(self, nome):
        with open(nome) as f:
            data = json.load(f)
        return data
    
    def json_para_linkedlist_despesa(self, nome):
        ficheiro = self.ler_ficheiro_json(nome)
        lista = DespesaslinkedList()
        orcamento = ficheiro[1]
        for i in ficheiro:
            if ficheiro[0] == i or ficheiro[1] == i:
                continue
            else:
                valor = i[0]
                data = i[1]
                categoria = i[2]
                descricao = i[3]
                despesa = Despesa(valor, data, categoria, descricao)
                lista.insert_last(despesa)
        return orcamento, lista
    
    @staticmethod
    def json_para_linkedlist_cliente():
        with open("Utilizadores.json") as f:
            ficheiro = json.load(f)
        lista = ClientLinkedList()
        for i in ficheiro:
            nome = i[0]
            senha = i[1]
            nif = i[2]
            cliente = Cliente(nome, senha, nif)
            lista.insert_last(cliente)
        return lista
    
    def linkedlist_para_json_despesa(self, nome, orcamento, linkedlist):
        utilizador = [nome]
        orcamento = [orcamento]
        self.escrever_ficheiro_json(f"{nome}.json", utilizador)
        self.escrever_ficheiro_json(orcamento, utilizador)
        for i in range(len(linkedlist)):
            elemento = linkedlist.remove_first()
            valor = elemento.get_valor()
            data = elemento.get_data()
            categoria = elemento.get_categoria()
            descricao = elemento.get_descricao()
            despesas = [valor, data, categoria, descricao]
            self.escrever_ficheiro_json(nome, despesas)

    @staticmethod
    def linkedlist_para_json_cliente(linkedlist):
        i = linkedlist
        nome = i.get_nome()
        senha = i.get_password()
        nif = i.get_nif()
        lista = [nome, senha, nif]
        json_string = json.dumps(lista)
        json_file = open("Utilizadores.json", 'a')
        json_file.write(json_string)
        json_file.close()
    
    

