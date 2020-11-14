logger_user = False

msg = 'Usuario Logado.' if logger_user else "Usuario precisa logar"

print(msg)

idade = int(input('Idade: '))
e_maior = (idade >= 18)

print("Pode acessar" if e_maior else "Não pode acessar")