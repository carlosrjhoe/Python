carrinho = []

carrinho.append(('arroz', 12.95))
carrinho.append(('feijão', 15.55))
carrinho.append(('macarrão', 10.95))
carrinho.append(('carne', 45.95))
carrinho.append(('biscoito', 2.95))
carrinho.append(('leite', 2.25))

total = 0

for produto in carrinho:
    total += produto[1]
    
print(f'O valor total é R${total:.2f}')
total_2 = sum([y for x, y in carrinho])
print(f'O valor total é R${total_2:.2f}')