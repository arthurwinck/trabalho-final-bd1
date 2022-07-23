from model.gerencia import Gerencia

class GerenciaView():
    def __init__(self):
        self.gerencia_helper = Gerencia()
    
    def crud(self, option):
        if(option == 11):
            print(self.gerencia_helper.list_all_equipe())
        elif(option == 12):
            nome = input("Digite o nome da equipe")
            ine = input("Digite o ine da equipe")
            print(self.gerencia_helper.insert_equipe(nome, ine))
        elif(option == 13):
            id_equipe = input("Digite o id da equipe que você quer deletar")
            print(self.gerencia_helper.delete_equipe(id_equipe))
        elif(option == 29):
            print(self.gerencia_helper.list_all_lotacao())
        elif(option == 30):
            id_profissional = input("Digite o id do profissional")
            id_equipe = input("Digite o id da equipe")
            print(self.gerencia_helper.insert_lotado(id_equipe, id_profissional))
        elif(option == 31):
            id_lotacao = input("Digite o id da lotação que você quer apagar")
            print(self.gerencia_helper.delete_lotado(id_lotacao))
