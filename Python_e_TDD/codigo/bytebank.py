from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    def nome(self):
        return self._nome.title()

    def salario(self):
        return self._salario

    def sobre_nome(self):
        nome_completo = self._nome.strip()
        sobre_nome = nome_completo.split(' ')
        return sobre_nome[-1].title()

    def idade(self):
        data_formatada = self._data_nascimento.split('/')
        ano = data_formatada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano)

    def eh_socio(self):
        sobrenomes = ['Conceição', 'Ramos', 'Andrade']
        return (self.sobre_nome() in sobrenomes)

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('O salário é muito alta para receber um bonus.')
        return valor

    def desconto(self):
        if self.sobre_nome():
            desconto = self._salario * 0.1
            self._salario = self._salario - desconto
            return self._salario

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'