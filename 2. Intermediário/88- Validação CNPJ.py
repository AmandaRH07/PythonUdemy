"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""
import re

def remove_caracteres(cnpj):
    """
    :param cnpj: valor do cnpj com caracteres denescesários
    :return: valor sem os caracteres especiais(/. -)
    """
    return re.sub(r'[^0-9]', '', cnpj)


def valida_primeiro_digito(cnpj, primeiro_digito):
    """
    :param cnpj: lista de números do cnpj
    :param primeiro_digito: contagem regressiva a partir do 5 até o 2 correspondente ao tamanho da lista de cnpjs
    :return: formula para conferir o primeiro número
    """

    multiplicacao = [int(i) * int(j) for i, j in zip(cnpj, primeiro_digito)]
    soma = sum(multiplicacao)

    formula = 11 - (soma % 11)

    if formula > 9:
        formula = 0

    return formula

def valida_segundo_digito(novo_cnpj, segundo_digito):
    """
    :param cnpj: lista de números do cnpj + o digito conferido na função valida_segundo_cnpj
    :param segundo_digito: contagem regressiva a partir do 6 até o 2 correspondente ao tamanho da lista de cnpjs
    :return: formula para conferir o segundo número
    """

    multiplicacao = [int(i) * int(j) for i, j in zip(novo_cnpj, segundo_digito)]
    soma = sum(multiplicacao)

    formula = 11 - (soma % 11)

    if formula > 9:
        formula = 0

    return formula

def verifica_cnpj(cnpj, novo_cnpj):
    if cnpj == novo_cnpj:
        print("cnpj valido")
    else:
        print("cnpj inválido")



def main():
    primeiro_digito = ["5", "4", "3", "2", "9", "8", "7", "6", "5", "4", "3", "2"]
    segundo_digito = ["6", "5", "4", "3", "2", "9", "8", "7", "6", "5", '4', "3", "2"]
    cnpj = []

    print("EX: 04.252.011/0001-10 548.762.565/5555-60")
    valor = input('Insira um CNPJ: ')

    sem_caracteres = remove_caracteres(valor)

    for i in sem_caracteres:
        cnpj.append(i)

    # removendo os dois ultimos digitos
    cnpj = cnpj[:-2]

    novo_cnpj = cnpj

    resultado1 = valida_primeiro_digito(cnpj, primeiro_digito)
    novo_cnpj.append(str(resultado1))

    resultado2 = valida_segundo_digito(novo_cnpj, segundo_digito)
    novo_cnpj.append(str(resultado2))

    verifica_cnpj(cnpj, novo_cnpj)

if __name__ == '__main__':
    main()
