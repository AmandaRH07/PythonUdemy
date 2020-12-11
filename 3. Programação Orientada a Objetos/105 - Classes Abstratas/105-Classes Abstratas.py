"""
Classes Abstratas
Métodos concretos: funcionam perfeitamente
Métodos abstratos: não tem nada dentro
"""

from abc import ABC, abstractclassmethod


class A(ABC):
    @abstractclassmethod
    def falar(self):
        pass

class B(A):
    def falar(self):
        print("Falando B")

b = B()
b.falar()

a = A()
a.falar()

