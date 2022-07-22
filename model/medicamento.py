from connect_sql import *
class medicamento():
    def __init__(self):
        self.conn = connect_sql('root', 'ThePassword', 'localhost', 'db_trabalho1')

    def list_all_medicamento(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Medicamento")
        return cursor.fetchall()
    
    def list_all_fabricante(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Fabricante")
        return cursor.fetchall()
    
    def insert_medicamento(self, nome, idFabricante):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO Medicamento (nome, idFabricante) VALUES (\"%s\", %s)""" % (nome, idFabricante))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique os dados cadastrados!"
        
    def insert_fabricante(self, nome):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO Fabricante (nome) VALUES (\"%s\")""" % (nome))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique os dados cadastrados!"
    
    def delete_fabricante(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM Fabricante WHERE idFabricante={}".format(id))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique se o paciente existe!"
    
    def delete_medicamento(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM Medicamento WHERE id_medicamento={}".format(id))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique se o paciente existe!"
    
