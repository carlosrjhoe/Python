import os

# Remover o arquivo com o banco de dados SQLite (caso exista)
os.remove("escola.db") if os.path.exists("escola.db") else None

import sqlite3

# criar uma conexão um banco de dados, se o banco de dados não existir, ele criará
con = sqlite3.connect("escola.db")

# Cursor permite percorrer todos os registros em um conjunto de dados
curso = con.cursor()

# Cria uma instrução SQL
sql_create = 'create table cursos'\
    '(id integer primary key, '\
    'titulo varchar(100), '\
    'categoria varchar(140))'

# Executa a instrução sql no cursor
curso.execute(sql_create)

# Instrução SQl para inserir registros
sql_insert = 'insert into cursos values (?, ?, ?)'

# Dados
recset = [(1000, 'Ciência de Dados', 'Data Science'),
          (1001, 'Big Data Fundamentos', 'Big data'),
          (1002, 'Python Fundamentos', 'Analise de Dados')]

# Inserindo registros
for registro in recset:
    curso.execute(sql_insert, registro)
    
# Gravar a transação (IMPORTANTE)
con.commit()

# Criando uma setença SQL para selecionar registros
sql_select = 'select * from cursos'

# Seleciona todos os registros e recupera os registros
curso.execute(sql_select)
dados = curso.fetchall()

# Mostrar
for linha in dados:
    print('Curso Id: %d, Título: %s, Categoria: %s' %linha)