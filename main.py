from view.paciente_view import PacienteView
from view.profissional_view import ProfissionalView
from view.gerencia_view import GerenciaView
from view.consulta_view import ConsultaView
from view.medicamento_view import MedicamentoView

from utils.gen import *

def autoinsert(paciente, profissional, gerencia, consulta, medicamento, num_inserts):
    error = []
    num_equipes = 5
    num_prof = int(num_inserts//4)

    # Inserção de pacientes
    print("Adicionando pacientes")
    for i in range(num_inserts):
        try:
            paciente.insert_paciente(gen_nome(), gen_nome(), gen_cpf(), gen_data_nasc())
        except Exception as e:
            print("Erro ao inserir pacientes")
            error.append(e)
            return error


    # Inserção das especialidades
    print("Adicionando especialidades")
    esp = ['Urologia', 'Neurologia', 'Psiquiatria', 'Pediatria', 'Oncologia', 'Nutrologia', 'Cirurgião Geral']
    for i in range(len(esp)):
        try:
            profissional.insert_especialidade(esp[i])
        except Exception as e:
            print("Erro ao inserir especialidades")
            error.append(e)
            return error

    # A relação entre profissionais e pacientes é de 1/4
    print("Adicionando profissionais")
    print(num_prof)
    for i in range(int(num_prof)):
        try:
            profissional.insert_profissional(gen_nome(), gen_cns(), gen_cpf())
        except Exception as e:
            print("Erro ao inserir profissionais")
            error.append(e)
            return error

    # Gerando 5 equipes
    print("Adicionando equipes")
    for i in range(num_equipes):
        try:

            gerencia.insert_equipe(gen_nome_equipe, gen_rand(1000,9999))
        except Exception as e:
            print("Erro ao inserir equipes")
            error.append(e)
            return error

    # Metade dos profissionais são médicos a outra metade dentistas
    print("Adicionando médicos e dentistas")
    for i in range(1, int(num_prof/2) + 1):
        try:
            profissional.insert_medico(gen_cfm_cfo(), i)
            profissional.insert_dentista(gen_cfm_cfo(), i+int(num_prof/2))
        except Exception as e:
            print("Erro ao inserir medicos e dentistas")
            error.append(e)
            return error

    # Metade dos profissionais tem especialidade
    print("Adicionando especialidades aos profissionais")
    for i in range(1, int(num_prof/2)+ 1):
        try:
            profissional.insert_profissional_especialidade(i, gen_rand(0, len(esp) - 1))
        except Exception as e:
            print("Erro ao inserir as relações nos profissionais")
            error.append(e)
            return error

    print("Adicionando lotações")
    for i in range(1, num_prof + 1):
        try:
            gerencia.insert_lotado(i % 5 + 1, i)
        except Exception as e:
            print("Erro ao inserir as lotações")
            error.append(e)
            return error

    print("Adicionando fabricantes")
    for i in range(5):
        try:
            medicamento.insert_fabricante(gen_nome_fabricante())
        except Exception as e:
            print("Erro ao inserir fabricantes")
            error.append(e)
            return error

    print("Adicionando medicamentos")
    for i in range(1, 21):
        try:
            medicamento.insert_medicamento(gen_nome_med(), i % 5 + 1)
        except Exception as e:
            print("Erro ao inserir medicamentos")
            error.append(e)
            return error

    # for i in range(20):
    #     print("Adicionando profissionais")
    #     try:
    #         medicamento.insert_medicamento(gen_nome_med(), i%5)
    #     except Exception as e:
    #         print("Erro ao inserir pacientes")
    #         error.append(e)
    #         return error
        
    print("Adicionando consultas")
    for i in range(1, num_inserts + 1):
        try:
            #Alterar data?
            consulta.insert_consulta(gen_data_cons(), i % num_prof + 1, i)
        except Exception as e:
            print("Erro ao inserir consultas")
            error.append(e)
            return error

    print("Adicionando receitas")
    for i in range(1, num_inserts + 1):
        try:
            horas = gen_rand(1,12)
            qtd = gen_rand(1,30)
            consulta.insert_receita(f"Toma medicação de {horas} em {horas} horas", i, qtd)
        except Exception as e:
            print("Erro ao inserir receitas")
            error.append(e)
            return error

    print("Adicionando relação receita medicamento")
    for i in range(1, num_inserts + 1):
        try:
            consulta.insert_receita_medicamento(i, i % 20 + 1)
        except Exception as e:
            print("Erro ao inserir medicamentos a receitas")
            print(i)
            error.append(e)
            return error

    return error


def init():

    paciente_view = PacienteView()
    profissional_view = ProfissionalView()
    gerencia_view = GerenciaView()
    consulta_view = ConsultaView()
    medicamento_view = MedicamentoView()

    error = autoinsert(paciente_view.paciente_helper, profissional_view.profissional_helper, gerencia_view.gerencia_helper, 
    consulta_view.consulta_helper, medicamento_view.medicamento_helper, 120)

    if len(error) != 0:
        print(error)
        print(error)
        return

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
        print("32-para listar receitas-medicamentos \n 33-para criar r-m \n 34-para excluir r-m")
        print("35-para lista profissional_especialidade \n 36-para criar profissional_especialidade \n 37-para excluir profissional_especialidade")
        option = int(input())

        
        paciente_view.crud(option)
        profissional_view.crud(option)
        gerencia_view.crud(option)
        consulta_view.crud(option)
        medicamento_view.crud(option)

main = init()