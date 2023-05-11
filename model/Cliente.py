import json

class Cliente:
    def __init__(self, nome, password, nif):
        self.__nome = nome
        self.__password = password
        self.__nif = nif

    def get_nome(self):
        return self.__nome
    def get_password(self):
        return self.__password
    def get_nif(self):
        return self.__nif
    def set_nome(self, nome):
        self.__nome = nome
    def set_password(self, password):
        self.__password = password
    def set_nif(self, nif):
        self.__nif = nif
    
