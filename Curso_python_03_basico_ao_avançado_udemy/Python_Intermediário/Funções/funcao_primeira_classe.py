"""
Higher order functions
Funçoes de primeira classe
"""

def saudacao(msg):
    return msg

def saudacao_2(saudacao):
    return saudacao

v = saudacao_2(saudacao)
print(v)