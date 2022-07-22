from connect_sql import *
class Consulta():

    def __init__(self):
        self.conn = connect_sql('root', 'ThePassword', 'localhost', 'db_trabalho1')

    def list_all_consulta(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Consulta")
        return cursor.fetchall()
    
    def list_all_receita(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Receita")
        return cursor.fetchall()

    def insert_consulta(self, data, medico, paciente):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO Consulta (data_hora, idProfissional, idPaciente) VALUES (DATE \'%s\', %s, %s)""" % (data, medico, paciente))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique os dados cadastrados!"

    def insert_receita(self, orientacao, idConsulta, quantidade_medicamento):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO Receita (orientacoes, qnt_medicamento, idConsulta) VALUES (DATE \'%s\', %s, %s)""" % (orientacao, idConsulta, quantidade_medicamento))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique os dados cadastrados!"
    
    
    def delete_consulta(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM Consulta WHERE idConsulta={}".format(id))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique se o paciente existe!"
    
    def delete_receita(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM Receita WHERE id_receita={}".format(id))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique se o paciente existe!"