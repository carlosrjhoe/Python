class Trabalahador:
    def __init__(self, nome, setor, ocupado=False):
        self.nome = nome
        self.setor = setor
        self.ocupado = ocupado

    def iniciar(self, hora=False):
        hora = hora
        if self.ocupado:
            print(f'{self.nome} do setor {self.setor} já está trabalhando,\n'
                  f'{self.nome} iniciou o expediente às {hora} horas.')
            return
        print(f'{self.nome} está trabalhando.')
        self.ocupado = True

    def encerrar(self, hora=False):
        if not self.ocupado:
            print(f'{self.nome} não está trabalhando.')
            return
        print(f'{self.nome} encerrou o expediente às {hora} horas.')
        self.ocupado = True

if __name__ == "__main__":
    funcionario01 = Trabalahador('carlos', 'ultilidades')
    funcionario01.encerrar('22')
    funcionario01.iniciar('12')
    funcionario01.iniciar('12')
    funcionario01.encerrar('22')