"""CRUD com PyMySQL no MSQl server
C- create
R - read
U - update
D - delete

pip install pymsql"""

import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password="Senha12345_",
        db='clientes',
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        print("conexão fechada")
        conexao.close()

# adicionar um cliente
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql= 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#              '(%s, %s, %s, %s)'
#         cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
#         conexao.commit()


# adicionar vários clientes ao mesmo tempo
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql= 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#              '(%s, %s, %s, %s)'
#
#         dados= [
#             ('MURIEL', 'FIGUEIREDO', '19', '55'),
#             ('ROSE', 'FIGUEIREDO', '19', '55'),
#             ('JOSE', 'FIGUEIREDO', '19', '55'),
#         ]
#         cursor.executemany(sql, dados)
#         conexao.commit()


# apagar cliente
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql= 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (6,))
#         conexao.commit()


# apagar vários clientes ao mesmo tempo
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN(%s, %s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9, 10))
#         conexao.commit()

# ou
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s and %s'
#         cursor.execute(sql, (11, 13))
#         conexao.commit()


# atualizar registro na base de dados
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql, ('EDUARDA', 5))
        conexao.commit()


with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            # print(linha['id'], linha['nome'], linha['sobrenome'])
            print(linha)
