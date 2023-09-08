from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def sobre_nome(self):
        nome_completo = self._nome.strip()
        sobre_nome = nome_completo.split(' ')
        return sobre_nome[-1]

    def idade(self):
        data_formatada = self._data_nascimento.split('/')
        ano = data_formatada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano)

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            valor = 0
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'

if __name__ == '__main__':
    carlos = Funcionario('carlos', '03/11/1985', 3139)
    print(type(carlos.nome))
    print(type(carlos._data_nascimento))
    print(type(carlos._salario))
    print(type(carlos.idade()))