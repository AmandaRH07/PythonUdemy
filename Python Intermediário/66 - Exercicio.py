# E - commerce

total = 0
carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))
carrinho.append(('Produto 4', 50))

soma = [ total + produtos[1] for produtos in carrinho ]

print(sum(soma))