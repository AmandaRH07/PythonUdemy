hora = input("Digite a hora:")

if hora.isdigit():
    hora = int(hora)

    if hora < 0 or hora > 23:
        print("Por favor, digite um horário entre 0 e 23 horas")
    else:
        if hora <= 11:
            print("Bom dia, dia")
        elif  hora <= 17:
            print("Boa tarde, Brasil,Boa noite Itália")
        else:
            print("Boa noite, vá dormir, você é piranha, não morcega")

