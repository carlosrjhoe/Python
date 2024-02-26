from classe import Pessoa

pessoa01 = Pessoa('carlos', 38, 370, 'M', 18.1)
pessoa02 = Pessoa('mayara', 39, 'R$280', 'F', 17.0)

pessoa01.desconto(15)
pessoa02.desconto(20)

print(pessoa01.preco)
print(pessoa02.preco)