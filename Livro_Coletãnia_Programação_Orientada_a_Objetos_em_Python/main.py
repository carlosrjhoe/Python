from contato import Contato, Cliente

cliente_01 = Cliente('carlos', 38)
cliente_01.addfone(35210079, 81995161616)
print(cliente_01.nome)
cliente_01.listaFone()