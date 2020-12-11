"""
Polimorfismo: classes derivadas de uma superclasse tenham métodos
iguais mas com comportamentos diferentes
"""

from abc import ABC, abstractclassmethod

class A(ABC):
    @abstractclassmethod
    def fala(self, msg):
        pass


class B(A):
    def fala(self, msg):
        print(f"B está falano{msg}")


class C(A):
    def fala(self, msg):
        print(f"C está falano{msg}")

b= B()
c =C()

b.fala("Um assunto")
c.fala("outro assunto")