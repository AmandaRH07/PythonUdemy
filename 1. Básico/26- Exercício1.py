i = input("Digite um número: ")



if i.isdigit():
    i = int(i)
    if i % 2 == 0:
        print("O número é par")
    else:
        print("O número é impar")
else:
    print("O número não é inteiro")
