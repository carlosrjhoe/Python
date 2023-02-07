import re

telefone = re.compile(r'\d\d\-\d\d\d\d-\d\d\d\d')
meu_telefone = telefone.search('Cell: 81-9555-9999, Trab: 21-9555-0000')
print(meu_telefone.group())