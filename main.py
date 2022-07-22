from view.paciente_view import PacienteView
from view.profissional_view import ProfissionalView

paciente_view = PacienteView()
profissional_view = ProfissionalView()
while True:

    print("___________________________")
    print("Escolha uma opção")
    print("1-Criar paciente \n 2-Deletar paciente\n 3-Listar paciente")
    print("4-listar profissionais \n 5- listar médicos \n 6-listar dentistas")
    print("7- criar profissionais \n 8 -criar médicos \n 9-criar dentista \n 10-Deletar profissionais relacionados")
    option = int(input())

    
    paciente_view.crud(option)
    profissional_view.crud(option)