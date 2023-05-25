import string
import datetime
import re

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



    def _toIntList(self, numstr):
        res = []
        for i in numstr:
            if i in string.digits:
                res.append(int(i))
        return res

    def _valN(self, num):
        num = self._toIntList(num)
        sum = 0
        for pos, dig in enumerate(num[:-1]):
            sum += dig * (9 - pos)
        return (sum % 11 and (11 - sum % 11) % 10) == num[-1]

    def controlNIF(self, nif):
        len_nif = 9
        if len(nif) != len_nif:
            return False
        if nif[0] not in "125689":
            return False
        return self._valN(nif)


    @staticmethod
    def valor_despesa(valor):
        try:
            valorfloat = float(valor)
        except ValueError:
            return False
        else:
            return valorfloat

    @staticmethod  
    def  categoria_despesas(descricao):
        try:
            categoria1 = float(descricao)
        except ValueError:
            return descricao
        else:
            return False
        
    @staticmethod
    def data_despesas(data):
        formato_data =  r'^\d{2}/\d{2}/\d{2}$'
        if  re.match(formato_data , data):
            try:
                dia, mes, ano = map(int, data.split('/'))
                datetime.datetime(year=ano, month=mes, day=dia)
            except ValueError:
                return False
            else:
                return dia, mes, ano
        else:
            return False
        
    @staticmethod
    def descrição_despesas(descricao):
        try:
            descricao1 = float(descricao)
        except ValueError:
            return descricao
        else:
            return False