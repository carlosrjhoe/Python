class Restaurante():
    
    def __init__(self, nome_restaurante, tipo_cozinha):
        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha
        
    def descricao_do_restaurante(self):
        print(f'O nome do restaurante: {self.nome_restaurante.title()} e tipo de conzinha é: {self.tipo_cozinha.title()}')
        
    def abrir_restaurante(self):
        print(f'O restaurante {self.nome_restaurante.title()} está aberto!')
    

class Usuarios():
    
    def __init__(self, primeiro_nome, segundo_nome, idade, sexo):
        self.primeiro_nome = primeiro_nome
        self.segundo_nome = segundo_nome
        self.idade = idade
        self.sexo = sexo  

    def perfil_usuario(self):
        print(f'Nome: {self.primeiro_nome.title()}\nSobre-nome: {self.segundo_nome.title()}\nIdade: {self.idade}\nSexo: {self.sexo.title()}')
        
    def saudadacao(self):
        print(f'Olá {self.primeiro_nome.title()}, seja bem vindo ao nosso restaurante.')
        


# carlos_restaurante = Restaurante('neto e luna', 'cazeira')
# may_restaurante = Restaurante('palacio de deus', 'gourme')
# neto_restaurante = Restaurante('casa da vovó', 'hamburgueria')

# carlos_restaurante.descricao_do_restaurante()
# carlos_restaurante.abrir_restaurante()

# may_restaurante.descricao_do_restaurante()
# may_restaurante.abrir_restaurante()

# neto_restaurante.descricao_do_restaurante()
# neto_restaurante.abrir_restaurante()

carlos = Usuarios('carlos', 'conceição', 36, 'm')
carlos.perfil_usuario()
carlos.saudadacao()

mayara = Usuarios('mayara', 'ramos', 37, 'f')
mayara.perfil_usuario()
mayara.saudadacao()