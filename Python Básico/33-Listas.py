#        0     1    2    3    4
lista = ['a', 'b', 'c', 'd', 'elefante']

print(lista)
print(lista[4])
print(lista[0:3]) # entre 0 e 3
print(lista[:3]) # antes do 3
print(lista[2:]) # depois do 2
print(lista[-1]) # ultimo da lista
print(lista[::2]) # pula dois elementos
print(lista[::-1]) # inverte os elementos

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l1)
print(l2)
print(l3)

l1.extend(l2)
print(l1)

l2.append('b')
print(l2[3])
l2.insert(0, 'banana')
print(l2)

l2.pop()
print(l2)

del(l3[3:5])
print(l3)

print(max(l3))
print(min(l3))
 
l4= list(range(1,10))
print(l4)

for valor in l4:
    print(valor)

secreto = 'perfume'
digitadas = []

while True: 
    letra = input("Digite uma letra: ")
    if len(letra) > 1:
        print("Ahhhh isso não vale, digite apenas uma letra.")
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f"Uhull, a letra '{letra}' existe na palavra secreta)")
    else:
        print(f"A letra '{letra}' não existe na palavra secreta")
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta  in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
   
    if secreto_temporario == secreto:
        print(f"Você ganhou!!! A palavra era: {secreto_temporario}")
        break
    else: 
        print (f"A palavra secreta está assim: {secreto_temporario}")
    
