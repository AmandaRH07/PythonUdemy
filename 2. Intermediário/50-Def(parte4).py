variavel = 'valor'

def func():
    print(variavel)

def func2():
    # sem o global, a variavel da func2 é outra variavel
    global variavel
    variavel = "outro valor"
    print(variavel)

func()
func2()

print(variavel)