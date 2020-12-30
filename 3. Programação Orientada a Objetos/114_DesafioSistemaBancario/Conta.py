from abc import ABC, abstractclassmethod


class Conta(ABC):
    def __init__(self, agencia, num_conta, saldo):
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo = self.saldo + valor
        return self.saldo

    def informacoes(self):
        print(f"""
            Agência: {self.agencia}
            Conta: {self.num_conta}
            Saldo: {self.saldo}""")

    def sacar(self, valor):
        if valor < self.saldo:
            self.saldo = self.saldo - valor
        else:
            print("Você não tem saldo suficiente para realizar um saque.")

        return self.saldo


class Conta_Poupanca(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
            return

        self.saldo -= valor
        self.informacoes()


class Conta_Corrente(Conta):
    def __init__(self, agencia, num_conta, saldo, limite=100):
        super().__init__(agencia, num_conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor > (self.saldo + self.limite):
            print("Saldo insuficiente")
            return

        self.saldo -= valor
        self.informacoes()
