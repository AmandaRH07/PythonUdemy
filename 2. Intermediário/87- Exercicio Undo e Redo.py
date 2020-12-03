"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa
"""

def adicionar_tarefa(lista_tarefas):
    add_info = input("\nInsira a tarefa a ser adicionada:\n")
    lista_tarefas.append(add_info)

def listar_tarefas(lista_tarefas):
    print("\nLista de tarefas")

    cont = 0
    for tarefa in lista_tarefas:
        cont += 1
        print(f"{cont}. {tarefa}")

def desfazer( lista_tarefas,ultimo_acaso):
    #ultima_acaso.append(lista_tarefas[len(lista_tarefas) - 1])
    #lista_tarefas.remove(lista_tarefas[len(lista_tarefas) - 1])
    ultima = lista_tarefas.pop()
    #lista_tarefas.pop()
    ultimo_acaso.append(ultima)

def refazer(ultimo_acaso,lista_tarefas):
    lista_tarefas.append(*ultimo_acaso)

def main():
    lista_tarefas =[]
    ultimo_acaso = []

    while True:
        opcao = input(f"""
        Menu
            1. Adicionar Tarefa
            2. Listar Tarefas
            3. Desfazer
            4. Refazer
            0. Sair
        Insira a opção desejada: """)

        if opcao == '1':
            adicionar_tarefa(lista_tarefas)

        elif opcao == '2':
            listar_tarefas(lista_tarefas)

        elif opcao == '3':
            desfazer(lista_tarefas, ultimo_acaso)

        elif opcao == '4':
            refazer(ultimo_acaso, lista_tarefas)

        elif opcao == '0':
            break

        else:
            print("Você inseriu uma opção inválida")



if __name__ == '__main__':
    main()
