"""Métodps Mágicos
https://rszalski.github.io/magicmethods/"""


class A:
    def __init__(self):
        print("init")

    def __new__(cls, *args, **kwargs):
        print("New")
        cls.nome = "amanda"

        def haha(*args, **kwargs):
            print("fala oi")

        cls.haha = haha

        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)

        return cls._jaexiste
        return super().__new__(cls)

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        resultado = 1
        for i in args:
            resultado *= i

        return resultado

    def __setattr__(self, key, value):
        print(key, value)
        if key == "nome":
            self.__dict__[key] = 'você não pode fazer isso'
        else:
            self.__dict__[key] = value

    def __str__(self):
        return "def str"


a = A()
a.haha()
print(a.nome)

variavel = a(1, 2, 3, 4, 5, nome="AManda")
print(variavel)

b = A()
c = A()
print(b == c)

a.nome = "Otavio"
a.qualquer = "224"
print(a.nome, a.qualquer)

print("STR: ", a)
