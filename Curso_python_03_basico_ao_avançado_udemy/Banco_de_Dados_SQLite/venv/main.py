import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conecta():
    """Se conectar com o servidor SQL"""
    conexao = pymysql.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
        db = 'clientes',
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        print('Conexão fechada')
        conexao.close()

with conecta() as conexao:
    with conexao.cursor() as cursor:
        """Inserir um registro no banco de dados"""
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s,%s,%s,%s)'
        cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
        conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         """Inserir mais de um registro no banco de dados de uma só vez"""
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s,%s,%s,%s)'
#         dados = [
#             ('ROBERTA','FIGUEIREDO','19','55',),
#             ('NETO','CONCEIÇÃO','7','27',),
#             ('LUNA','ROSENDO','5','25',),
#         ]
#         cursor.executemany(sql, dados)
#         conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         """Apagar registro um por vez"""
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (6,))
#         conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         """Apagar mais de um registro de uma vez"""
#         sql = 'DELETE FROM clientes WHERE id IN (%s,%s,%s)'
#         cursor.execute(sql, (1,2,3))
#         conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         """Apagar mais de um registro dentro de um intervalo"""
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (10,13))
#         conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         """Atualizar um registro"""
#         sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
#         cursor.execute(sql, ('JOANA', 14))
#         conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         """Mostrar todos os registro no banco de dados"""
#         cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')
#         resultado = cursor.fetchall()
        
#         for linha in resultado:
#             print(f'{linha}')

if __name__ == '__main__':
    conecta()