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
        