from model.profissional import Profissional

class ProfissionalView():
    def __init__(self):
        self.profissional_helper = Profissional()
    
    def crud(self, option):
        if(option == 4):
            print(self.profissional_helper.list_all())
        elif(option == 5):
            print(self.profissional_helper.list_all_med())
        elif(option == 6):
            print(self.profissional_helper.list_all_dent())
        elif(option == 7):
            nome = input("Digite o nome do profissional")
            cpf = input("Digite o cpf do profissional")
            cns = input("Digite o cns do profissional")
            print(self.profissional_helper.insert_profissional(nome, cpf, cns))
        elif(option == 8):
            idProfissional = input("Digite o id do profissional a ser relacionado")
            cfm = input("Digite o cfm do médico")
            print(self.profissional_helper.insert_medico(cfm, idProfissional))
        elif(option == 9):
            idProfissional = input("Digite o id do profissional a ser relacionado")
            cfo = input("Digite o cfo do dentista")
            print(self.profissional_helper.insert_dentista(cfo, idProfissional))
        elif(option == 10):
            id_profissional = input("Digite o id do profissional que você quer deletar")
            print(self.profissional_helper.delete_profissional_med(id_profissional))
            print(self.profissional_helper.delete_profissional_dent(id_profissional))
            print(self.profissional_helper.delete_profissional(id_profissional))
        elif(option == 26):
            print(self.profissional_helper.list_all_especialidade())
        elif(option == 27):
            titulo = input("Digite o titulo da especialidade")
            print(self.profissional_helper.insert_especialidade(titulo))
        elif(option == 28):
            id_esp = input("Digite o id da especialidade que você quer apagar")
            print(self.profissional_helper.delete_especialidade(id_esp))
        elif(option == 35):
            print(self.profissional_helper.list_all_profissional_especialidade())
        elif(option == 36):
            idProfissional = input("Digite o id do profissional")
            idEspecialidade = input("Digite o id da especialidade")
            print(self.profissional_helper.insert_profissional_especialidade(idProfissional, idEspecialidade))
        elif(option == 37):
            id_profissional_especialidade = input("Digite o id da relação profissional_especialidade que quer apagar")
            print(self.profissional_helper.delete_profissional_especialidade(id_profissional_especialidade))
        elif (option == 43):
            id = str(input("Insira o id do profissional: "))
            nome = str(input("nome: "))
            cns = str(input("cns: "))
            cpf = str(input("cpf: "))
            print(self.profissional_helper.update_profissional(id, nome, cns, cpf))