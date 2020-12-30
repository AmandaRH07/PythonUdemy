"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
"""

from Cliente import Cliente
from Conta import Conta, Conta_Corrente, Conta_Poupanca


def main():
    while True:

        opcao = int(input("""
        BANCO
            1. Criar uma conta
            2. Visualizar dados de conta
            3. Depositar
            4. Sacar
            0. Sair
        Insira a opção desejada: """))


        if opcao == 1:
            nome_cliente = input("\nNome: ")
            idade_cliente = input("Idade: ")
            cliente = Cliente(nome_cliente, idade_cliente)

            opcao_banco = input("""
                Escolha o banco
                    1. Caixa
                    2. Itau
                    3. Bradesco
                Em qual banco você gostaria de de criar a conta? """)

            if opcao_banco < '1' or opcao_banco > '3':
                print("Você escolheu um banco inválido. Por favor tente novamente!")
                pass
            else:
                opcao_conta = input("""
                    1. Conta Poupança
                    2. Conta Corrente
                    Escolha o tipo de conta: """)

                if opcao_conta == "1":
                    conta = Conta_Poupanca(opcao_banco, 1234, 2000)

                elif opcao_conta == "2":
                    conta = Conta_Corrente(opcao_banco, 1234, 2000)

                else:
                    pass

            cliente.inserir_conta(conta)

        elif opcao == 2:
            conta.informacoes()

        elif opcao == 3:
            deposito = float(input("""Insira o valor a ser depositado: """))
            conta.deposito(deposito)

        elif opcao == 4:
            saque = float(input("""Insira o valor a ser sacado: """))
            conta.sacar(saque)

        elif opcao == 0:
            print("Saiu")
            break

        else:
            pass


if __name__ == '__main__':
    main()
