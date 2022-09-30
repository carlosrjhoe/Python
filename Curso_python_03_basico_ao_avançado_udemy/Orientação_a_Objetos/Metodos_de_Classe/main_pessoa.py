from Pessoa import Pessoa

carlos = Pessoa('carlos', 37)
mayara = Pessoa.por_ano_nascimento('mayara', 37, 1985)
print(carlos.idade)
carlos.get_ano_nascimento()
print(carlos.gera_id())