class Banco:
    def __init__(self):
        self.agencias = [1, 2, 3]
        self.clientes = []
        self.contas = []

    def novo_cliente(self, cliente):
        self.clientes.append(cliente)

    def nova_conta(self, conta):
        self.contas.append(conta)
