from queries.paciente import Paciente



paciente_helper = Paciente()

while True:

    print("___________________________")
    print("Escolha uma opção")
    print("1-Criar paciente \n 2-Deletar paciente\n 3-Listar paciente")
    option = int(input())

    if(option == 1):
        paciente_res = input("Digite o responsável pelo paciente")
        nome = input("Digite o nome do paciente")
        cpf = input("Digite o cpf do paciente")
        data_nascimento = input("Digite a data de data_nascimento do paciente")
        print(paciente_helper.insert_paciente(paciente_res, nome, cpf, data_nascimento))
    
    if(option == 2):
        id_paciente = int(input("Digite o id do paciente que quer excluir"))
        print(paciente_helper.delete_paciente(id_paciente))
    
    if(option == 3):
        print(paciente_helper.list_all())