from typing import TypedDict

class Programa(TypedDict):
    versao: str
    revisao: float

if __name__ == '__main__':
    projeto = Programa(versao='1.03.237', revisao=0.01)
    print(projeto)
    print(type(projeto))
    