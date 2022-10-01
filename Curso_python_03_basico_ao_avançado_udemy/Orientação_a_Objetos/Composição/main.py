from classes import Cliente

pessoa_01 = Cliente('carlos', 36)
pessoa_01.inserir_endereco('cabo de santo agostinho','pe')
print(f'{pessoa_01.nome}')
pessoa_01.listar_enderecos()

pessoa_02 = Cliente('mayara', 37)
pessoa_02.inserir_endereco('cabo de santo agostinho', 'pe')
print(f'{pessoa_02.nome}')
pessoa_02.listar_enderecos()

