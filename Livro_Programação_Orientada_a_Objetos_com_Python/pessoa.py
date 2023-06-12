# class Pessoa:
#     pass

# p1 = Pessoa()
# p1.Nome = "Carlos"
# p1.Idade = 37
# p1.Documentos = {"Identidade": 476888955, "CPF": 16019931447}
# p1.Pais = ["Carlos Roberto", "Maria Rosiclé"]

# print(f'{p1.Nome}')
# print(f'{p1.Idade}')
# print(f'{p1.Documentos}')
# print(f'{p1.Pais}')


# class Pessoa:

#     def acao(self):
#         print("Ação 1 sendo executada.")

# if __name__ == '__main__':

#     pessoa1 = Pessoa()
#     pessoa1.acao()

# class Pessoa:
#     # print("Classe pessoa em execução.")
#     def __init__(self, nome, idade, sexo="Não encontrado. ", altura="Não encontrado. "):
#         # print("Instancia da class Pessoa em execução.")
#         self.nome = nome
#         self.idade = idade
#         self.sexo = sexo
#         self.altura = altura

#     def dados(self):
#         print(f"Bem vindo {self.nome}, sua idade é {self.idade}, seu sexo é {self.sexo}, e você tem {self.altura}m de altura.")

# if __name__ == '__main__':
#     p1 = Pessoa("Carlos",37,"M",1.81)
#     p1.dados()


class Pessoa:
    def __init__(self, name, login=False, logoff=False):
        self.name = name
        self.login = login
        self.logout = logoff

    def logar(self):
        if self.login:
            print(f"Você já está logado, {self.name}.")
            return 

        print(f"Bem vindo {self.name}, você está logado no sistemas")
        self.login = True

    def deslogar(self):
        if not self.login:
            print(f"{self.name} você não está logado no sistema.")
            return
        print(f"{self.name} Foi deslogado do sistema.")
        self.login = False

if __name__ == "__main__":
    p1 = Pessoa("Carlos")
    p1.logar()
    p1.logar()
    p1.deslogar()
    # p1.deslogar()