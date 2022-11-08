import sqlite3

conexao = sqlite3.connect('base_de_dados.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Carlos", 84.5) ')
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Mayara", 70.5)')
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Neto", 27.7)')
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Luna", 24.3)')
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Emilly", 54.3)')
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Lúcia", 96.7)')
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Rose", 70.8)')
# conexao.commit()

# cursor.execute(
#     'UPDATE clientes SET nome=:nome WHERE id=:id',
#     {'nome': 'Valdênia', 'id': 5}    
# )
# conexao.commit()

# cursor.execute(
#     'DELETE FROM clientes WHERE id=:id',
#     {'id': 6}    
# )
# conexao.commit()




cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso', {'peso': 50})
print('Maior que 50kg:')
for linha in cursor.fetchall():
    nome, peso = linha
    print(f'Nome: {nome}, Peso: {peso}kg')

cursor.execute('SELECT nome, peso FROM clientes WHERE peso < :peso', {'peso': 50})
print('\nMenor que 50kg:')
for linha in cursor.fetchall():
    nome, peso = linha
    print(f'Nome: {nome}, Peso: {peso}kg')

cursor.close()
conexao.close()