import sqlite3

class AgendaDB:
    def __init__(self, arquivo):
        self.coneccao = sqlite3.connect(arquivo)
        self.cursor = self.coneccao.cursor()
        
    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.coneccao.commit()
    
    def editar(self, id, nome, telefone):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (id, nome, telefone))
        self.coneccao.commit()
    
    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.coneccao.commit()
    
    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')
        for linha in self.cursor.fetchall():
            print(f'{linha}')
    
    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))
    
    def fechar(self):
        self.cursor.close()
        self.coneccao.close()
        
if __name__ == '__main__': 
    agenda = AgendaDB('agenda.db')
    agenda.editar(1,'luna ramos cordeiro', '81995419951')
    agenda.editar(2,'mayara ramos cordeiro', '81911112222')
    agenda.editar(6,'carlos roberto conceicao neto', '81922223333')
    agenda.editar(7,'carlos roberto conceicao junior', '81933334444')
    agenda.buscar('conceicao')