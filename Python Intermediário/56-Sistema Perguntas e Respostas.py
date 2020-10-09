perguntas = {
    'Pergunta 1':{
        'pergunta': 'Quanto é 2+2?',
        'respostas': {
            'a': '1','b': '4','c': '3','d': '2',},
        'resposta_certa': 'b',
    },
    'Pergunta 2':{
        'pergunta': 'Quanto é 5*3?',
        'respostas': {
            'a': '9','b': '10','c': '15','d': '25',},
        'resposta_certa': 'c',
    },
    'Pergunta 3':{
        'pergunta': 'Quanto é 20/4?',
        'respostas': {
            'a': '4','b': '6','c': '10','d': '5',},
        'resposta_certa': 'd',
    },
     'Pergunta 4':{
        'pergunta': 'Quanto é 35-15?',
        'respostas': {
            'a': '20','b': '15','c': '10','d': '34',},
        'resposta_certa': 'a',
    },
     'Pergunta 5':{
        'pergunta': 'Quanto é 4^4?',
        'respostas': {
            'a': '4','b': '16','c': '8','d': '12',},
        'resposta_certa': 'b',
    },
}

print()

respostas_certas = 0 
# K(key) e V(value)
for pk, pv in perguntas.items():
    print(f"{pk}: {pv['pergunta']}")

    print("Escolha a opção correta: ")
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input("Sua resposta: ")

    if resposta_usuario == pv['resposta_certa']:
        print("Parabéns!!!! Você acertou!!!")
        respostas_certas += 1
    else:
        print("Ixiiii. Você errou!!!")
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f"""Você acertou {respostas_certas} resposta(s).
Sua porcentagem de acerto foi de {porcentagem_acerto:.2f}%""")