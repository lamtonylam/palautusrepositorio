# ÄLÄ MUUTA TÄMÄN LUOKAN KOODIA
class Maksukortti:
    def __init__(self, saldo):
        self.__saldo = saldo

    def lataa(self, maara):
        self.__saldo = self.__saldo + maara

    def osta(self, maara):
        self.__saldo = self.__saldo - maara

    def saldo(self):
        return self.__saldo
