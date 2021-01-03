import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT  or IGNORE INTO agenda (nome, telefone) VALUES (?,?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE or IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE from agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute("SELECT * FROM agenda")

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'

        #(f'%{valor}%') -> que tenha o valor em qualquer lugar no nome
        self.cursor.execute(consulta, (f'%{valor}%',))

        print(f"BUSCAR: {valor}")
        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')

    # agenda.inserir("Amanda", '123456')
    # agenda.inserir("Maria", '654321')
    # agenda.inserir("Joao", '123654')
    # agenda.inserir("Gilherme", '321456')
    # agenda.inserir("Eduarda", '321654')

    # agenda.editar('Yago', '213456', 10)

    print("Listar antes de excluir ")
    agenda.listar()

    agenda.excluir(10)

    print("Listar depois de excluir ")
    agenda.listar()

    agenda.inserir("Maria Eduarda", '101010')
    agenda.inserir("Maria Paula", '0101010')
    agenda.inserir("Maria Luiza", '111000')
    agenda.inserir("R. Luiza", '000111')
    agenda.inserir("Maria Luiza meio do caminho", '101100')

    agenda.buscar('Luiza')
