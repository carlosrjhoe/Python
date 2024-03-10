class Menssgens:
    def mensagem_1(self):
        print('Inicializando o sistema')

    def mensagem_2(self):
        print('Encerrando o sistema')

class Gatilho:
    def __init__(self):
        self.msg = Menssgens()

    def msg_1(self):
        return self.msg.mensagem_1()

    def msg_2(self):
        return self.msg.mensagem_2()

    def __getattr__(self, mensagem):
        return getattr(self.msg, mensagem)

if __name__ == "__main__":
    operacao_1 = Gatilho()
    operacao_1.msg_1()
    operacao_1.mensagem_2()