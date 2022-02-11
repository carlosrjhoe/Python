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
            raise ValueError("CPF inválido!")
        
        
    def __str__(self) -> str:
        '''A forma correta da epresentação de uma str dentro de uma classe.'''
        return self.format_cpf()
    
    def cpf_e_valido(self, documento):
        '''Método que validará o CPF'''
        if len(documento) == 11:
            return True
        else:
            return False
        
    def format_cpf(self):
        '''Aqui estou fatiando o strings do CPF, para formata-lo no formato padrão Brasileiro'''
        fatia_um = self.cpf[:3]
        fatia_dois = self.cpf[3:6]
        fatia_tres = self.cpf[6:9]
        fatia_quatro = self.cpf[9:]
        return f'{fatia_um}.{fatia_dois}.{fatia_tres}-{fatia_quatro}'