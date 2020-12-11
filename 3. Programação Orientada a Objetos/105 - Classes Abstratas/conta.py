from abc import ABC, abstractclassmethod

class Conta(ABC):
    def __init__(self,agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa ser numérico. ")

        self._saldo = valor

    def depositar(self, valor):
        if isinstance(valor, (int, float)):
            raise ValueError("Depósito precisa ser numérico. ")

        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f"Agência: {self.agencia}", end="")
        print(f"Conta: {self.conta}", end="")
        print(f"Saldo: {self.saldo}")

    @abstractclassmethod
    def sacar(self, valor):
        self.detalhes()
