from random import randint

class Pessoa:
    ano_atual = 2020

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #Método de instancia
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    #Método de classe
    @classmethod
    # não precisa do self
    # CLS = class -> convenção
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome,idade)

    #Método estático
    #Não precisa nem da instancia nem da classe
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

#Método de instancia
p1 = Pessoa("Joice", 32)
print(p1.idade)
p1.get_ano_nascimento()

#Método de classe
p2 = Pessoa.por_ano_nascimento("Ana", 1981)
print(p2)
print(p2.nome, p2.idade)

#Método Estático
print(p1.gera_id())