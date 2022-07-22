from model.paciente import Paciente

class PacienteView():
    def __init__(self):
        self.paciente_helper = Paciente()
    
    def crud(self, option):
        if(option == 1):
            paciente_res = input("Digite o responsável pelo paciente")
            nome = input("Digite o nome do paciente")
            cpf = input("Digite o cpf do paciente")
            data_nascimento = input("Digite a data de data_nascimento do paciente")
            print(self.paciente_helper.insert_paciente(paciente_res, nome, cpf, data_nascimento))
    
        if(option == 2):
            id_paciente = int(input("Digite o id do paciente que quer excluir"))
            print(self.paciente_helper.delete_paciente(id_paciente))
        
        if(option == 3):
            print(self.paciente_helper.list_all())