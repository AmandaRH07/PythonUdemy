# Associação = Usa

from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor("Joao")
caneta = Caneta("Bic")
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()

