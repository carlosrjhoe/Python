from validate_docbr import CPF

class Documento:
    
    @staticmethod
    def criar_novo(documento):
        doc_str = str(documento)
        if len(doc_str) == 11:
            return DocCpf(doc_str)
        if len(doc_str) == 14:
            return DocCnpj(doc_str)
        if len(doc_str) == 20:
            return DocQualquer(doc_str)
        else:
            raise ValueError('Documento incorreto.')
        
    
    
        
        
class Cpf:
    
    def __init__(self, documento):
        '''O método	__init__() é responsável por inicializar o objeto'''
        '''Faremos essa validação no momento em que estamos instanciando a classe, colocando-a dentro de __init__() recebendo self e documento também. Passaremos o documento como str para não nos preocuparmos com as aspas, e adicionaremos self.cpf_eh_Valido() do documento.'''
        self.documento = str(documento)
        if self.cpf_e_valido(documento):
            self.cpf = documento
            print('CPF é válido')
        else:
            '''Se este não for igual ao documento, lançaremos uma exceção ValueError() com a mensagem "CPF invalido!".'''
            return ValueError('CPF inválido')
        
        
    def __str__(self):
        '''A forma correta da epresentação de uma str dentro de uma classe.'''
        return self.format_cpf()
    
    def cpf_e_valido(self, documento):
        '''Método que validará o CPF'''
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError('Quantidade de digitos inválida')
        
    def format_cpf(self):
        '''Aqui estou fatiando o strings do CPF, para formata-lo no formato padrão Brasileiro'''
        mascara = CPF()
        return mascara.mask(self.documento)