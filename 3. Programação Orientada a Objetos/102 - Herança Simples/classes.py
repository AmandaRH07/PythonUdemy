class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f"{self.nomeclasse}: Falando")

class Aluno(Pessoa):
    # def __init__(self, nome, idade):
    #     self.nome = nome
    #     self.idade = idade
    def estudar(self):
        print(f"{self.nomeclasse}: estudando")

class Cliente(Pessoa):
    def comprar(self):
        print(f"{self.nomeclasse}: comprando")

    def falar(self):
        print("Está em cliente")

# Sobreposição de membros
class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        #Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        #super().falar()
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f"{self.nome} {self.sobrenome}")
