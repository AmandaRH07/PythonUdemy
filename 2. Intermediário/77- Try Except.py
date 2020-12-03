"""
Try e Except = tratamento de excessão
error aparece todos os erros disponíveis
"esperar" dar o erro e tratar o erro certo
"""

try:
    #a = []
    a = {}
    print(a[1])
except NameError as erro:
    print("error", erro)
except (IndexError, KeyError) as erro:
    print("erro de indice ou chave")
except Exception as erro:
    print(("Ocorreu um erro inesperado"))
else:
    #executado quando não tem mais erro
    print("chegou no else")
finally:
    print("finalmente")