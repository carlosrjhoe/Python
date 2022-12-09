import requests

class Pessoa:
    def __init__(self, name, sobrenome):
        self.name = name
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obter_todos_os_dados(self):
        resposta = requests.get('https://github.com/carlosrjhoe')

        if resposta.ok:
            return 'CONECTADO'
        else:
            return 'ERRO 404'
        