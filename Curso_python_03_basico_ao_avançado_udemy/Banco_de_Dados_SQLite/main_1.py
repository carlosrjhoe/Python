import sqlite3

# Objéto de conecção
conexao = sqlite3.connect('base_de_dados.db')
# Objéto de cursor 
cursor = conexao.cursor() 

# Criar tabela
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

# Incerir um registro
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ("Carlos Roberto", 84.4))
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ("Mayara Ramos", 70.5))
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ("Carlos Neto", 27))
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ("Luna Ramos", 25))
# conexao.commit()

# Alterar registro
# cursor.execute(
#     'UPDATE clientes SET nome=:nome WHERE id=:id',
#     {'id': 2, 'nome': 'Emilly', 'peso': 57}
# )
# conexao.commit()

# Excluir um registro (UMA VEZ EXCLUIDO, NÃO TEM COMO RECUPERAR!!!)
# cursor.execute(
#     'DELETE FROM clientes WHERE id=:id',
#     {'id': 2}
# )
# conexao.commit()

# Pesquisa detalhada
cursor.execute('SELECT nome, peso FROM clientes WHERE peso >= :peso',
               {'peso': 35})

# Mostrar todos os valores
# cursor.execute('SELECT * FROM clientes')

# Buscar todos os valores
print(f'Maior que 35kg')
for linha in cursor.fetchall():
    nome, peso = linha
    print(f'Nome: {nome} - Peso: {peso}kg')


cursor.close()
conexao.close()