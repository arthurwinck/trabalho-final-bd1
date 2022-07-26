from view.consultas_especiais_view import ConsultasEspView
from view.paciente_view import PacienteView
from view.profissional_view import ProfissionalView
from view.gerencia_view import GerenciaView
from view.consulta_view import ConsultaView
from view.medicamento_view import MedicamentoView

from utils.autoinsert import *

def init():

    paciente_view = PacienteView()
    profissional_view = ProfissionalView()
    gerencia_view = GerenciaView()
    consulta_view = ConsultaView()
    medicamento_view = MedicamentoView()
    consultas_especiais_view = ConsultasEspView()

    while True:

        print("___________________________")
        print("Escolha uma opção")
        print("1-Criar paciente \n 2-Deletar paciente\n 3-Listar paciente")
        print("4-listar profissionais \n 5- listar médicos \n 6-listar dentistas")
        print("7- criar profissionais \n 8 -criar médicos \n 9-criar dentista \n 10-Deletar profissionais relacionados")
        print("11- Para listar as equipes do hospital \n 12- para criar uma nova equipe \n 13 - para deletar uma equipe")
        print("14- para listar consultas \n 15- para listar receitas \n 16 - para inserir consulta \n 17-para inserir receita \n 18 - para deletar consultas \n 19 - para deletar receitas")
        print("20-para listar medicamentos \n 21-para listar fabricantes \n 22-para inserir medicamento \n 23-para inserir fabricante \n 24- para deletar medicamento \n 25- para deletar fabricante")
        print("26-para listar especialidade \n 27-para criar especialidade \n 28-para deletar uma especialidade")
        print("29-para listar lotacao \n 30-para criar lotacao \n 31-para deletar lotacao")
        print("32-para inserir receitas-medicamentos \n 33-para deletar r-m \n 34-para listar r-m")
        print("35-para lista profissional_especialidade \n 36-para criar profissional_especialidade \n 37-para excluir profissional_especialidade")
        print("38-consulta 1 - seção 6")
        print("39-consulta 2 - seção 6")
        print("40-consulta 3 - seção 6")
        print("41-inserir dados aleatórios")
        print("42-editar paciente")
        print("43-editar profissional")
        print("44-editar consulta")
        print("45-editar medicamento")
        print("46-editar receita")



        option = int(input())

        paciente_view.crud(option)
        profissional_view.crud(option)
        gerencia_view.crud(option)
        consulta_view.crud(option)
        medicamento_view.crud(option)
        consultas_especiais_view.crud(option)

        error = autoinsert(paciente_view.paciente_helper, profissional_view.profissional_helper, gerencia_view.gerencia_helper, 
        consulta_view.consulta_helper, medicamento_view.medicamento_helper, 120, option)

main = init()