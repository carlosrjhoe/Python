class Pessoa:

    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def apresentacao(self):
        print(f'Nome: {self.nome.title()}')
        print(f'Idade: {self.idade}')
        print(f'Profissão: {self.profissao.title()}')

carlos = Pessoa('carlos', 37, 'lider de manutenção')
mayara = Pessoa('mayara', 37, 'analista de rh')

carlos.apresentacao()
mayara.apresentacao()