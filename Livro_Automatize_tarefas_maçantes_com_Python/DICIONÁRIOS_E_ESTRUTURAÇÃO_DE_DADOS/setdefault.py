from pprint import pprint

msg = "Era um dia claro e frio de abril e os relógios marcavam treze horas."

cont = {}

for i in msg:
    # O programa percorre todos os caracteres da string contida na variável message em um loop, contabilizando cada caractere presente.
    cont.setdefault(i, 0)
    cont[i] = cont[i] + 1

# A função pprint.pprint() é especialmente útil quando o dicionário contém listas ou dicionários aninhados
pprint(cont)