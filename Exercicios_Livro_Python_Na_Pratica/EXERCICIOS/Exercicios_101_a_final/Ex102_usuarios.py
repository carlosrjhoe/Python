class Usuarios:
    nome = 'usuario'
    senha = 'padrao'
    
    def __init__(self, nome=None, senha=None) -> None:
        texto = 'Programa para mostar usuario'
        print(f'{"#"*len(texto)}')
        print(f'{texto.center(len(texto))}')
        print(f'{"#"*len(texto)}')
        
        self.nome = nome
        self.senha = senha
        
    def mostar_usuario(self):
        print(f'Usuario: {self.nome}\nSenha: {self.senha}\nRegistrado com sucesso!')
        