import re
class ExtratorURL:
    
    def __init__(self, url):
        """Salva a url em um atributo do objeto (self.url = url) e verifica se a url é válida"""
        self.url = self.sanitiza_url(url)
        self.valida_url()
        
    def sanitiza_url(self, url):
        """Retorna a url removendo espaços em branco."""
        if type(url) == str:
            return url.strip()
    
    def valida_url(self):
        """Valida se a url está vazia"""
        if not self.url:
            raise ValueError('A url está vazia...')
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError('A URL não é válida.')
        print('A URL é válida!')

    def get_url_base(self):
        """Retorna a base da url."""
        indice_interrogacao = self.url.find('?')
        url_base = self.url[0:indice_interrogacao]
        return url_base
    
    def get_url_parametros(self):
        """Retorna os parâmetros da url."""
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao+1:36]
        return url_parametros
    
    def get_valor_parametro(self, paramentro_de_busca):
        """Retorna o valor do parametro `parametro_busca`."""
        paramentro_de_busca = 'quantidade'
        indice_paramentro = self.get_url_parametros().find(paramentro_de_busca)
        indice_valor = indice_paramentro + len(paramentro_de_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro('url')

'''
METODO FIND():
    Determina se a string str ocorre em string, ou em uma substring de string se o índice inicial beg e o índice final end forem fornecidos.

    Sintaxe
    url.find('?')
    
METODO LEN()
    A função retorna o número de itens em um objeto.
    Quando o objeto é uma string, a len()função retorna o número de caracteres na string.
    
    Sintaxe
    len(object)
    
METODO REPLACE():
    A função substitui uma parte do texto por uma outra String. A palavra replace(), do Inglês, siginifca substituir e é isso que a função replace() da classe String do Python faz.
    
    Sintaxe
    url.replace("aa", "123")
    
METODO STRIP():
    O função remove caracteres da esquerda e da direita com base no argumento (uma string que especifica o conjunto de caracteres a ser removido).
    
    Sintaxe
    url = url.strip()
    
METODO RAISE:
    A raisepalavra-chave é usada para gerar uma exceção. Você pode definir que tipo de erro gerar e o texto a ser impresso para o usuário.

MODULO RE: # Expressão Regulares
    re.compile(): 
    também aceita um argumento opcional flags, utilizados para habilitar vários recursos especiais e variações de sintaxe. Nós vamos ver todas as configurações disponíveis mais tarde, mas por agora, um único exemplo vai servir:
    
    match():
    Determina se a RE combina com o início da string.
'''