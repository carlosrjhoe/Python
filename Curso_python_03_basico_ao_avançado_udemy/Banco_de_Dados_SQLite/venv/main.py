import pymysql.cursors

conexao = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    db='clientes',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with conexao.cursor() as cursor:
    cursor.execute('SELECT * FROM clientes LIMIT 50')
    resultado = cursor.fetchall()
    for linha in resultado:
        print(f'{linha}')
    
conexao.close()