#def = definir funções

def funcao(mensagem):
    print("Hello World!")
    print(mensagem)
    print()

funcao('Mensagem')

def saudacao(mensagem = 'Olá', nome = 'Usuário'):
    mensagem= mensagem.replace('O', '#')
    print(mensagem, nome)
    return f'{mensagem} {nome}'

saudacao()
saudacao(nome = "Sara", mensagem = "E ai")
saudacao("Marcia")
saudacao('Oi')
saudacao('Olá', "Maria")
variavel = saudacao()