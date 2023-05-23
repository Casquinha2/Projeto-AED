import string

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