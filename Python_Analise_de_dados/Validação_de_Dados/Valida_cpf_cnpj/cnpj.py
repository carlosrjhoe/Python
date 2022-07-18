from validate_docbr import CNPJ

meu_cnpj = '26373828293'
cnpj = CNPJ()
print(cnpj.validate(meu_cnpj))