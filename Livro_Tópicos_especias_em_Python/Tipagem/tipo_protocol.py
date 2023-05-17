from typing import Protocol

class Pessoa(Protocol):
    nome: str

def identificacao(primeiro_nome: Pessoa) -> str:
    print(f'Usuário identificado como: {primeiro_nome.nome}')

class Pessoa1:
    nome = 'Carlos'


if __name__ == '__main__':
    pessoa1 = Pessoa1()
    identificacao(pessoa1)
    print(type(pessoa1))    