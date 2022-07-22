from model.medicamento import Medicamento

class MedicamentoView():
    def __init__(self):
        self.medicamento_helper = Medicamento()

    def crud(self, option):
        if(option == 20):
            print(self.medicamento_helper.list_all_medicamento())
        elif(option == 21):
            print(self.medicamento_helper.list_all_fabricante())
        elif(option == 22):
            nome = input("Digite o nome do medicamento")
            Fabricante = input("Digite o id do fabricante")
            print(self.medicamento_helper.insert_medicamento(nome, Fabricante))
        elif(option == 23):
            nome = input("Digite o nome do fabricante")
            print(self.medicamento_helper.insert_fabricante(nome))
        elif(option == 24):
            id_medicamento = input("Digite o id do medicamento que quer deletar")
            print(self.medicamento_helper.delete_medicamento(id_medicamento))
        elif(option == 25):
            id_fabricante = input("Digite o id do fabricante que quer deletar")
            print(self.medicamento_helper.delete_fabricante(id_fabricante))
            