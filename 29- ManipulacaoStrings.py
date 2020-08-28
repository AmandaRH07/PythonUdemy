#positivos [012345678]
texto    = "Python s2"
#negativos-[987654321]
# print(texto[2])
# print(texto[9])

novaString = texto[:6]  # fatiar a string
print(novaString)
novaString = texto[7:]  # começa do final
print(novaString)

novaString = texto[-9:-3]  # ao contrário
print(novaString)

novaString = texto[0::3]  # pula
print(novaString)

print(len(texto))