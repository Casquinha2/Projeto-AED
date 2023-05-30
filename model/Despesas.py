class Despesa:
    def __init__(self, valor, data, categoria, descricao):
        self.valor = valor
        self.data = data
        self.categoria = categoria
        self.descricao = descricao

    def get_valor(self):
        return self.valor
    def get_data(self):
        return self.data
    def get_categoria(self):
        return self.categoria
    def get_descricao(self):
        return self.descricao
    def set_valor(self, valor):
        self.valor = valor
    def set_data(self, data):
        self.data = data
    def set_categoria(self, categoria):
        self.categoria = categoria
    def set_descricao(self, descricao):
        self.descricao = descricao
        
# tiago explica
#tiago explicação: esta função é para o utilizador não conseguir criar uma despesa que irá ultrapassar o orçamento mensal
    @staticmethod
    def despesa_valida(valor, linkedlist, orcamento):
        despesa = 0
        for i in range(linkedlist.size):
            despesa += linkedlist.get(i).get_valor()
        if orcamento == 0:
            return True
        elif despesa + valor <= orcamento:
            return True
        else:
            return False
        
    @staticmethod
    def verificar_limite(limite, despesa, linkedlist, orcamento):
        for i in range(linkedlist.size):
            despesa += linkedlist.get(i).get_valor()
        if despesa < limite and limite > orcamento:
            return True
        else:
            return False
        
   
    @staticmethod
    def verificar_limite(limite, despesa, linkedlist, orcamento):
        limite = (limite * 100)/orcamento
        for i in range(linkedlist.size):
            despesa += linkedlist.get(i).get_valor()
        if despesa < limite:
            return True
        else:
            return False

       
