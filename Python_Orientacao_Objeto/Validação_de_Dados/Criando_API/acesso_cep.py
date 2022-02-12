import requests
'''biblioteca requests para fazermos requisições HTTP ao ViaCEP'''

class BuscaEndereco:
    '''Valida e busca CEP'''
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError('Cep inválido!')
        
    def __str__(self) -> str:
        return self.format_cep()
    
    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
        
    def format_cep(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'
    
    '''Acessamos uma API usando a biblioteca REQUESTS'''
    def acessa_via_cep(self):
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        
        '''O método GET retorna informações de algum recurso.'''
        r = requests.get(url)
        
        '''biblioteca requests para para acessar a API do "ViaCEP" e converter o retorno para json.'''
        dados = r.json()
        
        '''extrair as informações desejadas da variável dados.'''
        return (
            dados['localidade'],
            dados['uf'],
            dados['cep'],
            dados['bairro'],
            dados['logradouro'],
            dados['complemento']
        )
        