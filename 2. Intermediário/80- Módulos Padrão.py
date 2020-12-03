"""
Módulos Padrão Python
Módulos são arquivos .py e servem para expandir
as funcionalidades padão da linguagem
https://docs.python.org/3/py-modindex.html
"""
#sys não é o foco, mas sim os módulos
import sys
#from sys import platform  #--> importa direto o necessaário
from random import randint as randint_original
#from random import * importa tudo e pode fazer bagunça
from random import randint, random

#import pymysql
# no terminal: pip pymsql

print(sys.platform)

# dessa forma sobreescreve, não acontece se só importar
def randint(*args):
    return "hahahaha"
print(randint())

# precisa dar um "apelido" com o as
print(randint_original(0,10))
print(random())


