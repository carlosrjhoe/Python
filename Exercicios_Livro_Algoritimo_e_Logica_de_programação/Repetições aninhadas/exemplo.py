"""Listagem 5.15 – Impressão de tabuadas"""
tabuada = 1
while tabuada <= 10:
    numero = 1
    while numero <= 10:
        print(f'{tabuada} x {numero} = {tabuada*numero}')
        numero += 1
    tabuada += 1
    print('#' * 20)
