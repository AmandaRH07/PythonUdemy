"""
    Outras linguagens: Public, protected, private
    Python:
        fica oculto mais ainda pode acessar:
        _protected
        recomendado fortemente que não acesse:
        __privado
"""

class BaseDados:
    def __init__(self):
        self.__dados = {}

    #para obter um dado
    @property
    def dados(self):
        return self.__dados

    def inserir_clientes(self, id, nome):
        if "clientes" not in self.__dados:
            self.__dados["clientes"] = {id:nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id,nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDados()
#bd._dados = "outra coisa"
bd.inserir_clientes(1, "Ana")
bd.inserir_clientes(2, "Maria")
print(bd.dados)
#bd.__dados = "outra coisa"
#print(bd.__BaseDados_dados)
bd.lista_clientes()

# Sem private
# bd.inserir_clientes(1, "Ana")
# bd.inserir_clientes(2, "Maria")
# bd.inserir_clientes(3, "Renata")
# bd.dados = "outra coisa"
# bd.apaga_cliente(2)
# bd.lista_clientes()
# #print(bd.dados)
