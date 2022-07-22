from connect_sql import *
class Paciente():
    def __init__(self):
        self.conn = connect_sql('root', 'ThePassword', 'localhost', 'db_trabalho1')

    def list_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Paciente")
        return cursor.fetchall()
    
    def insert_paciente(self, paciente_resp, nome, cpf, data_nascimento):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO Paciente (paciente_resp, nome, cpf, data_nascimento) VALUES (\"%s\", \"%s\", \"%s\", DATE \'%s\')""" % (paciente_resp, nome, cpf, data_nascimento))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            print(e)
            return "Algo errado ocorreu, verifique os dados cadastrados!"
    
    def delete_paciente(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM Paciente WHERE idPaciente={}".format(id))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique se o paciente existe!"
    
