class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))




    #Getter = obter o valor
    @property
    def preco(self):
        # por convenção e para não gerar loop por _variavel na frente da variável
        return self._preco

    #Setter = devolve o valor
    @preco.setter
    def preco(self, valor):
        if isinstance(valor,str):\
            valor  = float(valor.replace("R$", ""))
            #replace = substituit o R$ para nada
        self._preco = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,valor):
        self._nome = valor.title()

p1 = Produto("CAMISETA", 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto("CANECA", "R$15")
p2.desconto(10)
print(p2.nome, p2.preco)