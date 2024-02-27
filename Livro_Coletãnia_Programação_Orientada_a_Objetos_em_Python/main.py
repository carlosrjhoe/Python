from basesedados import BaseDeDados

relClientes = BaseDeDados()
relClientes.inserir('carlos', 123456789)
relClientes.inserir('mayara', 12345687689)
relClientes.inserir('neto', 1234539369)
relClientes.inserir('luna', 1234539276)
relClientes.listar()

relClientes.__base = 'Novo Banco de dados'
print(relClientes._baseDeDados__base)
print(relClientes.__base)