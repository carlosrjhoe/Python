"""8.5 – Cidades: Escreva uma função chamada describe_city() que aceite o
nome de uma cidade e seu país. A função deve exibir uma frase simples, como
Reykjavik está localizada na Islândia. Forneça um valor default ao
parâmetro que representa o país. Chame sua função para três cidades diferentes
em que pelo menos uma delas não esteja no país default"""

def descricao_das_cidades(nome_cidade, texto='fica no meio do caminho entre Recife e Porto de Galinhas, a menos de 45 minutos da capital.\n', nome_pais='E fica no Brasil\n'):
    print(f'A cidade de {nome_cidade}, {texto}, {nome_pais}.')
    
descricao_das_cidades('Cabo de santo Agostinho')
descricao_das_cidades('Pontes dos carvalhos', 'é um distrito do município brasileiro de Cabo de Santo Agostinho, litoral sul do estado de Pernambuco, Grande Recife.')
descricao_das_cidades('Lisboa','é uma cidade e um município português, capital de Portugal e da Área Metropolitana de Lisboa.', 'Portugal')