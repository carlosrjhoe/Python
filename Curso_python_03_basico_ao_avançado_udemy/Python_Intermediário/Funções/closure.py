"""
Função que retorna outra função
"""


def saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}"

    return saudar


saudacao_bom_dia = saudacao("Bom dia")
saudacao_boa_noite = saudacao("Boa Noite")

for nome in ["carlos", "mayara"]:
    print(f"{saudacao_bom_dia(nome.title())}")

for nome in ["neto", "luna"]:
    print(f"{saudacao_boa_noite(nome.title())}")
