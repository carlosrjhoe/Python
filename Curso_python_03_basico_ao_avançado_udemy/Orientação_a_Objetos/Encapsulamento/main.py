from BaseDeDados import BaseDeDados
    
bd = BaseDeDados()
bd.inserir_cliente(1, 'carlos')
bd.inserir_cliente(2, 'mayara')
bd.inserir_cliente(3, 'neto')
bd.inserir_cliente(4, 'luna')
bd.apagar_cliente(2)
bd.listar_dados()