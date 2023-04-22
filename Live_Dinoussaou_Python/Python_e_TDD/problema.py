"""
Numeros = [3, 4, 5, 0, 1, -14, 20, 2, 7, 10, -2]
"""
from typing import List

def problema(numeros: List[int]) -> int:
    valores_filtrados = list(filter(lambda x: x > 0, sorted(numeros)))

    if not valores_filtrados:
        return 1
    
    r = range(valores_filtrados[0], valores_filtrados[-1])

    for i, j in zip(valores_filtrados, r):
        if i != j:
            return j