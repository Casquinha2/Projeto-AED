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
    
    @staticmethod
    def json_para_linkedlist_despesa(nome):
        with open(f"{nome}.json", "w") as f:
            ficheiro = json.load(f)
        lista = DespesaslinkedList()
        orcamento = ficheiro[1][0]
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
    def json_para_linkedlist_cliente(linkedlist):
        with open("Utilizadores.json") as f:
            ficheiro = json.load(f)
        if ficheiro == []:
            return linkedlist
        else:
            for i in ficheiro:
                nome = i[0]
                senha = i[1]
                nif = i[2]
                cliente = Cliente(nome, senha, nif)
                linkedlist.insert_last(cliente)
            return linkedlist
    
    @staticmethod
    def linkedlist_para_json_despesa(nome, orcamento, linkedlist):
        lista_pai = []
        utilizador = [nome]
        orcamento = [orcamento]
        lista_pai.append(utilizador)
        lista_pai.append(orcamento)
        for i in range(linkedlist.size):
            elemento = linkedlist.remove_first()
            valor = elemento.get_valor()
            data = elemento.get_data()
            categoria = elemento.get_categoria()
            descricao = elemento.get_descricao()
            despesas = [valor, data, categoria, descricao]
            lista_pai.append(despesas)
        json_string = json.dumps(lista_pai)
        json_file = open(f"{nome}.json", 'w')
        json_file.write(json_string)
        json_file.close()

    @staticmethod
    def linkedlist_para_json_cliente(linkedlist, tamanho):
        lista_pai = []
        for f in range(tamanho):
            i = linkedlist.get(f)
            nome = i.get_nome()
            senha = i.get_password()
            nif = i.get_nif()
            lista = [nome, senha, nif]
            lista_pai.append(lista)
        json_string = json.dumps(lista_pai)
        json_file = open("Utilizadores.json", 'w')
        json_file.write(json_string)
        json_file.close()