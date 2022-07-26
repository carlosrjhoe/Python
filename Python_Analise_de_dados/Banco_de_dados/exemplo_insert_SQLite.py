import sqlite3

# Criar conexão
conn = sqlite3.connect("dsa.db")

# Criando cursor
c = conn.cursor()

# Função para criar uma tabela
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, prod_mane TEXT, valor REAL)')
    
# Função para inserir um linha
def data_insert():
    c.execute("INSERT INTO produtos VALUES(10, '2022-7-26', 'Teclado', 90)")
    conn.commit()
    c.close()
    conn.close()
    
# Criar tabela
create_table()

# Inserir dados
data_insert()