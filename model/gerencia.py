from connect_sql import *
class Gerencia():

    def __init__(self):
        self.conn = connect_sql('root', 'ThePassword', 'localhost', 'db_trabalho1')

    def list_all_equipe(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Equipe")
        return cursor.fetchall()
    
    def list_all_lotacao(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Lotado")
        return cursor.fetchall()
    

    def insert_equipe(self, nome, ine):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO Equipe (nome, ine) VALUES (\"%s\", \"%s\")""" % (nome, ine))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique os dados cadastrados!"
    
    def insert_lotado(self, id_departamento, id_profissional):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO Lotado (id_departamento, id_profissional) VALUES (%s, %s)""" % (id_departamento, id_profissional))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique os dados cadastrados!"
    
    
    def delete_equipe(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM Equipe WHERE id_departamento={}".format(id))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique se o paciente existe!"
    
    def delete_lotado(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM Lotado WHERE id_lotado={}".format(id))
            self.conn.commit()
            return "Sucesso"
        except Exception as e:
            return "Algo errado ocorreu, verifique se o paciente existe!"
    
    
    

    