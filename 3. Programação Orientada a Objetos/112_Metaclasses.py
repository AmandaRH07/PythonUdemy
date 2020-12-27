"""
Metaclasses
Em Python tudo é objeto, incluindo classes
Metaclasses são classes que criam classes
Ex: type é uma metaclasse
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        print(name)
        if name == "A":
            return type.__new__(mcs, name, bases, namespace)
        print(namespace)

        if "b_fala" not in namespace:
            print(f"Você precisa criar o método b_fala em {name}")
        else:
            if not callable(namespace['b_fala']):
                print(f"b_fala precisa ser um métoo, não um atributo em {name}")
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    def fala(self):
        self.b_fala()


class B(A):
    teste = "Valor"
    # b_fala = "teste"
    # pass

    def b_fala(self):
        print("OI")

    def sei_la(self):
        pass


b = B()
b.fala()

class Pai:
    nome = 'teste'

C = type(
    'c',
    (Pai,),
    {'attr': "Ola mundo"}
)

c = C()
print(type(c))
print(c.nome)