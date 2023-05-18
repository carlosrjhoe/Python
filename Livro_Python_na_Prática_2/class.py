from dataclasses import dataclass

@dataclass(frozen=True)
# aqui tendo seu parâmetro frozen configurado para True, para que de fato os objetos sobre o escopo desse       marcador sejam imutáveis após sua criação.
class Cachorro:
    cor: str
    idade: int

if __name__ == '__main__':
    pet = Cachorro('Preto e branco', 6)
    pet.cor = 'amarelo'
    print(pet.cor)
    print(pet.idade)