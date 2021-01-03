"""Usando o módulo sqlite3 do SQlite"""

import sqlite3

conexao = sqlite3.connect("basededados.db")
cursor = conexao.cursor()

# criar tabelas
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

# formas de inserir registros
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ("Maria", 50))
#
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#                {'nome': 'João', 'peso': 25})
#
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',
#                {'id': None, 'nome': 'Daniel', 'peso': 90})

# executar as alterações
conexao.commit()

# alterar valores adicionados
cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id',
               {'nome': 'Joana', 'id': 2})

conexao.commit()

# apagar valor !!CUIDADO!!
# cursor.execute('DELETE FROM clientes WHERE id=:id ',
#                {'id': 2})


# mostrar valores
cursor.execute('SELECT * FROM clientes')

# cursor.fetchall()
for linha in cursor.fetchall():
    identificador, nome, peso = linha

    print(identificador, nome, peso)

print()

# mosrtrar valores específicos
cursor.execute('SELECT nome,peso FROM clientes WHERE peso >:peso',
               {'peso': 50})

for linha2 in cursor.fetchall():
    nome, peso = linha2

    print(nome,peso)

cursor.close()
conexao.close()
