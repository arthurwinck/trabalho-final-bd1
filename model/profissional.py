from connect_sql import *
class Profissional():

    def __init__(self):
        self.conn = connect_sql('root', 'ThePassword', 'localhost', 'db_trabalho1')

    def list_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Profissional")
        return cursor.fetchall()
    
    def list_all_med(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Medico")
        return cursor.fetchall()
    
    def list_all_dent(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Dentista")
        return cursor.fetchall()
    
    def list_all_especialidade(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Especialidade")
        return cursor.fetchall()
    
    def list_all_profissional_especialidade(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Profissional_especialidade")
        return cursor.fetchall()

    def insert_profissional(self, nome, cns, cpf):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO Profissional (nome, cpf, cns) VALUES (\"%s\", \"%s\", \"%s\")""" % (nome, cpf, cns))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique os dados cadastrados!"
    
   
    def insert_medico(self, CFM, idProfissional):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO Medico (CFM, idProfissional) VALUES (\"%s\", %s)""" % (CFM, idProfissional))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique os dados cadastrados!"
    
    def insert_dentista(self, CFO, idProfissional):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO Dentista (CFO, idProfissional) VALUES (\"%s\", %s)""" % (CFO, idProfissional))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique os dados cadastrados!"
    
    def insert_especialidade(self, titulo):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO Especialidade (titulo) VALUES (\"%s\")""" % (titulo))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique os dados cadastrados!"
    
    def insert_profissional_especialidade(self, idProfissional, idEspecialidade):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO Profissional_especialidade (idProfissional, idEspecialidade) VALUES (%s, %s)""" % (idProfissional, idEspecialidade))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique os dados cadastrados!"
    
    def delete_profissional(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM Profissional WHERE idProfissional={}".format(id))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique se o paciente existe!"
    
    def delete_profissional_med(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM Medico WHERE idProfissional={}".format(id))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique se o paciente existe!"
    
    def delete_profissional_dent(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM Dentista WHERE idProfissional={}".format(id))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique se o paciente existe!"
    
    def delete_especialidade(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM Especialidade WHERE idEspecialidade={}".format(id))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique se o paciente existe!"
    
    def delete_profissional_especialidade(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM Profissional_especialidade WHERE possui_id={}".format(id))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique se o paciente existe!"
    

    
