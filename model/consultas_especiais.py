from connect_sql import *
from model.consulta import Consulta

class Consulta_Esp():

    def __init__(self):
        self.conn = connect_sql('root', 'ThePassword', 'localhost', 'db_trabalho1')

    def consulta_1(self):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT Especialidade.titulo, COUNT(*) from Profissional JOIN Profissional_especialidade on Profissional.idProfissional = Profissional_especialidade.idProfissional JOIN Especialidade
        on Especialidade.idEspecialidade = Profissional_especialidade.idEspecialidade JOIN Consulta on Consulta.idProfissional = Profissional.idProfissional GROUP by Especialidade.idEspecialidade ORDER BY COUNT(*) DESC;
        """)
        return cursor.fetchall()
    
    def consulta_2(self):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT Equipe.nome, COUNT(*) FROM Equipe join Lotado on Equipe.id_departamento = Lotado.id_departamento JOIN Profissional on Profissional.idProfissional = Lotado.id_profissional JOIN
        Consulta on Consulta.idProfissional = Profissional.idProfissional GROUP by Equipe.id_departamento ORDER by COUNT(*) DESC;
        """)
        return cursor.fetchall()

    def consulta_3(self):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT Medicamento.nome, AVG(Receita.qtd_medicamento) as media from Medicamento NATURAL JOIN Receita_medicamento NATURAL JOIN Receita GROUP by Medicamento.id_medicamento ORDER BY media DESC;""")
        return cursor.fetchall()

