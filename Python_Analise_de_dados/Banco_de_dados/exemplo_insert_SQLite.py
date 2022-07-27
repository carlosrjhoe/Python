import sqlite3
import random
import time
import datetime
import os

# Remover o arquivo com o banco de dados SQLite (caso exista)
os.remove("dsa1.db") if os.path.exists("dsa1.db") else None

# Criar conexão
conn = sqlite3.connect("dsa1.db")

# Criando cursor
c = conn.cursor()

# Função para criar uma tabela
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, prod_name TEXT, valor REAL)')
    
# Função para inserir um linha
def data_insert():
    c.execute("INSERT INTO produtos VALUES('2022-7-26 12:34:45', 'Teclado', 90.00)")
    conn.commit()
    c.close()
    conn.close()
    
# Usando variaveis para inserir dados
def data_insert_var():
    new_date = datetime.datetime.now()
    new_prod_name = 'Monitor'
    new_valor = random.randrange(50, 100)
    c.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (? ,? ,?)", (new_date, new_prod_name, new_valor))
    conn.commit()

# Gerando valores e inserindo na tabela
for i in range(10):
    data_insert_var()
    time.sleep(1)
    
# Encerrando a conexão
c.close()
conn.close()

# Criar tabela
# create_table()

# Inserir dados
# data_insert()