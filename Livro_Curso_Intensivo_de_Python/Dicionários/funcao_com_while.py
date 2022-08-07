def caracteristicas(primeiro_nome, segundo_nome, idade=''):
    """Devolve um dicionário com informações sobre uma pessoa."""
    pessoa = {'Primeiro': primeiro_nome, 'Segundo': segundo_nome}
    if idade:
        pessoa['idade'] = idade
    return pessoa

# Loop infinito
while True:
    print('\nPor favor diga seu nome:')
    print('Digite [q] para sair do laço infinito.')
    P_nome = input('Primeiro nome: ')
    if P_nome == 'q':
        """A instrução break permite um modo simples de sair do laço
        em qualquer prompt:"""
        break
        
    S_nome = input('Segundo nome: ')
    if S_nome == 'q':
       break
   
    nome_formatado = caracteristicas(P_nome, S_nome)
    
    print(f'Olá, {nome_formatado}')