class Cachorro():
    
    def __init__(self, dono, nome, idade):
        self.dono = dono
        self.nome = nome
        self.idade = idade
      
    def sentar(self):
        print(f'{self.nome.title()} senta agora...')
        
    def rolar(self):
        print(f'{self.nome.title()} rolar no chão agora...')
        

meu_cachorro = Cachorro('carlos','fred',3)
cachorro_de_may = Cachorro('may','tufik', 5)


print(f'{meu_cachorro.dono.title()} é o dono do {meu_cachorro.nome.title()}, e seu cão tem {meu_cachorro.idade} anos.')
print(f'{cachorro_de_may.dono.title()} é a dona do {cachorro_de_may.nome.title()}, e seu cão tem {cachorro_de_may.idade} anos de idade.')
meu_cachorro.rolar()
meu_cachorro.sentar()