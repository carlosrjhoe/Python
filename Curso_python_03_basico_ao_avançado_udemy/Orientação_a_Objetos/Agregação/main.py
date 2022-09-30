from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

produto_01 = Produto('celular', 3000)
produto_02 = Produto('camisa', 30)
produto_03 = Produto('caneca', 15)

carrinho.inserir_produto(produto_01)
carrinho.inserir_produto(produto_02)
carrinho.inserir_produto(produto_03)

carrinho.lista_produtos()
carrinho.soma_total()