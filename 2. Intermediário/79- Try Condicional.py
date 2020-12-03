"""
Uso de exceções como condicionais
"""
def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while True:
    numero = converte_numero(input("Digite um número: "))
    # se o número não for vazio
    if numero is not None:
        print(numero + 5)
    else:
        print("Isso não é número")