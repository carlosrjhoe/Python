from typing import final

# @final
class Pessoa:
    @final
    def acao(self):
        print('Trabalhando...')

if __name__ == '__main__':
    pessoa1 = Pessoa()
    pessoa1.acao()