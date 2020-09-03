variavel = ["Amanda hass", "Imariazinha"]

comeca_com_m = False
for valor in variavel:
    if valor.lower().startswith('m'):
       break
else:
    print("Não existe uma palavra que começa com M")