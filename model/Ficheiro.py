import json
from model.DespesasLinkedList import *
from model.Despesas import *
from model.Cliente import *
from model.ClientLinkedList import *

class Ficheiro:
    @staticmethod
    def json_para_linkedlist_despesa(nome):
        with open(f"{nome}.json", "r") as f:
            ficheiro = json.load(f)
        lista = DespesaslinkedList()
        orcamento = ficheiro[1][0]
        limite = ficheiro[2][0]
        for i in ficheiro:
            if ficheiro[0] == i or ficheiro[1] == i or ficheiro[2] == i:
                continue
            else:
                valor = i[0]
                data = i[1]
                categoria = i[2]
                descricao = i[3]
                despesa = Despesa(valor, data, categoria, descricao)
                lista.insert_last(despesa)
        return orcamento, limite, lista
    
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
    def linkedlist_para_json_despesa(nome, orcamento, limite, linkedlist):
        lista_pai = []
        utilizador = [nome]
        orcamento = [orcamento]
        limite = [limite]
        lista_pai.append(utilizador)
        lista_pai.append(orcamento)
        lista_pai.append(limite)
        for i in range(linkedlist.size):
            elemento = linkedlist.get(i)
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