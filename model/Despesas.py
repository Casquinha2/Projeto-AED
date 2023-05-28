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

    