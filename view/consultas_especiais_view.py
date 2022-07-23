from model.consultas_especiais import Consulta_Esp

class ConsultasEspView():
    def __init__(self):
        self.consultas_especiais_helper = Consulta_Esp()
    
    def crud(self, option):
        if(option == 38):
            print(self.consultas_especiais_helper.consulta_1())
        elif(option == 39):
            print(self.consultas_especiais_helper.consulta_2())
        elif(option == 40):
            print(self.consultas_especiais_helper.consulta_3())
        