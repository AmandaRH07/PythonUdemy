while True:
    minha_string = input('Digite uma frase: ')
    tamanho_sring = len(minha_string)

    cont = 0
    contagem_atual = 0;
    letra = ''
    while cont < tamanho_sring:
        qtt_vezes = minha_string.count(minha_string[cont])
        #strip remove os espaços do começo e do fim
        if contagem_atual < qtt_vezes and minha_string[cont].strip():
            letra = minha_string[cont]
            contagem_atual = qtt_vezes
        cont += 1
    print(letra, contagem_atual)

########################
# nova_string=''
# print(minha_string.count('a'))
# while cont < tamanho_sring:
#     if minha_string[cont] == 'r':
#         # pass
#         nova_string= nova_string + minha_string[cont].upper()
#     else:
#         nova_string = nova_string+ minha_string[cont]
#     # print(cont,minha_string[cont])
#     cont+=1
# print(nova_string)
