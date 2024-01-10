# language:pt

Funcionalidade: Soma
"""
Sendo um usário Eu quero somas dois números para que seja possível receber seu resultado.
"""

Cenário: Soma de inteiros positivos
    Quando somar "2" e "2"
    Então o resultado deve ser "4"

Cenário: Soma de inteiros negativos
    Quando somar "-3" e "-3"
    Então o resultado deve ser "-6"
