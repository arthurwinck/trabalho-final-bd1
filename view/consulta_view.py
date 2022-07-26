from model.consulta import Consulta

class ConsultaView():
    def __init__(self):
        self.consulta_helper = Consulta()
    
    def crud(self, option):
        if(option == 14):
            print(self.consulta_helper.list_all_consulta())
        elif(option == 15):
            print(self.consulta_helper.list_all_receita())
        elif(option == 16):
            data = input("Digite a data da consulta, no formato YYYY-MM-DD")
            paciente = input("Digite o id do paciente")
            profissional = input("Digite o id do profissional")
            print(self.consulta_helper.insert_consulta(data, profissional, paciente))
        elif(option == 17):
            orientacao = input("Digite as orientações para a receita")
            id_consulta = input("Digite o id da consulta relacionada")
            quantidade_medicamento = input("Digite a quantidade de medicamento que deve ser tomada")
            print(self.consulta_helper.insert_receita(orientacao, id_consulta, quantidade_medicamento))
        elif(option == 18):
            id_consulta = input("Digite o id da consulta que você quer apagar")
            print(self.consulta_helper.delete_consulta(id_consulta))
        elif(option == 19):
            id_receita = input("Digite o id da receita que você quer apagar")
            print(self.consulta_helper.delete_receita(id_receita))
        elif(option == 32):
            id_receita = input("Selecione o id da receita")
            id_medicamento = input("Selecione o id do medicamento")
            print(self.consulta_helper.insert_receita_medicamento(id_receita, id_medicamento))
        elif(option == 33):
            id_receita_medicamento = input("Digite o id da relação receita-medicamento que você quer excluir")
            print(self.consulta_helper.delete_receita_medicamento(id_receita_medicamento))
        elif(option == 34):
            print(self.consulta_helper.list_all_receita_medicamento())
        
        elif (option == 44):
            id = input("Digite o id da consulta")
            data = input("Data da consulta")
            medico = input("Medico da consulta")
            paciente = input("Paciente da consulta")
            print(self.consulta_helper.update_consulta(id, data, medico, paciente))
        elif (option == 46):
            id = input("Digite o id: ")
            orientacao = input("Digite a orientação: ")
            qtd_med = input("Digite a quantidade de med: ")
            id_consulta = input("Digite o id da consulta")
            print(self.consulta_helper.update_receita(id, orientacao, id_consulta, qtd_med))