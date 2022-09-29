from datetime import datetime

class Pessoa:
    # Variavel da Classe
    data = datetime.now()
    
    def __init__(self, nome, nascimento, comendo=False, falar=False):
        """" Método construtor, possui a responsabilidade de criar o objeto da classe, neste caso, Pessoa."""
        texto = 'Brincando com Orientação a Objetos com Python'
        print(f'{"#"*len(texto)}')
        print(f'{texto.center(len(texto))}')
        print(f'{"#"*len(texto)}')
        self.nome = nome
        self.nascimento = nascimento
        self.comendo = comendo
        self.falar = falar
        
    
    def get_idade(self):
        """Irá calcular e retornar a idade do objeto."""
        self.idade = int(self.data.year - self.nascimento)
        return self.idade
    
    def falando(self, assunto):
        """Irá verificar se o atributo (comendo) está verdadeiro, se estiver, o objeto irá falar."""
        if self.comendo:
            print(f'{self.nome.title()} Está comendo, não pode falar de boca cheia.')
            return
        
        print(f'{assunto}')
        self.comendo = False
        
    def informacao(self):
        """Irá mostar as informações do objeto instaciado."""
        print(f'{self.nome.title()} nasceu em {self.nascimento}, e tem {self.get_idade()} anos.')
    
    def comer(self, alimento):
        """Íra verificar se o atributo (comendo) do objeto instanciado está comendo"""
        if self.comendo:
            print(f'{self.nome.title()} já está comendo.\n')
            return
        
        print(f'{self.nome.title()} está comendo {alimento}.')
        self.comendo = True
        
    def para_de_comer(self):
        """Íra verificar se o atributo (comendo) do objeto está comendo, se estiver, o objeto irá parar de comer."""
        if not self.comendo:
            print(f'{self.nome.title()} Não está comendo.')
            return
        
        print(f'{self.nome.title()} Parou de comer.')
        self.comendo = False