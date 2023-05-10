import json

class Cliente:
    def __init__(self, nome, senha, nif):
        self.__nome = nome
        self.__senha = senha
        self.__nif = nif

    def get_nome(self):
        return self.__nome
    def get_senha(self):
        return self.__senha
    def get_nif(self):
        return self.__nif
    def set_nome(self, nome):
        self.__nome = nome
    def set_senha(self, senha):
        self.__senha = senha
    def set_nif(self, nif):
        self.__nif = nif
    
