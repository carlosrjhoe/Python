from typing import Union

def soma(num1: int, num2: int) -> Union[str, int]:
    res_soma = num1 + num2
    return res_soma

def novaSoma(num1: Union[str, float], num2: Union[int, float]) -> Union[str, int]:
    res_soma = num1 + num2
    print(f'O resultado da soma é: {res_soma}')
    return res_soma

if __name__ == '__main__':
    print(soma(99, 12))
    novaSoma(99, 12)
