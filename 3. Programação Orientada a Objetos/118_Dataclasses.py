"""O que são dataclasses? O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python.
Leia a documentação: https://docs.python.org/pt-br/3/library/dataclasses.html
"""

from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple


"""
eq (comparação não funciona.Ex: 1 == 1
order (sorted não funciona)
frozen (não deixa alterar nada na classe)
init (não le o init)"""

@dataclass(eq=True, order=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)

    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise TypeError(
                f'Tipo inválido {type(self.nome).__name__} != str em {self}'
            )

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa("A", "Luiza")
p2 = Pessoa("C", "Luiza")
p3 = Pessoa("E", "Luiza")
p4 = Pessoa("B", "Luiza")
p5 = Pessoa("D", "Luiza")
# p6 = Pessoa(123, "Luiza")

print(p1)
print(p1.nome)
print(p1.sobrenome)
print(p1.nome_completo)

print(p1 == p2)

pessoas = [p1, p2, p3, p4, p5]
print(sorted(pessoas))

print(asdict(p1))
print(astuple(p1))
