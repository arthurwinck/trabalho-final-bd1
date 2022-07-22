import names
import random as rd

def gen_rand(a, b):
    return rd.randint(a,b)


def gen_nome():
    return names.get_full_name()

def gen_cpf():
    # Não possui nenhuma validação
    num = rd.randrange(1,10**9)
    return (9 - len(str(num)))*'0' + str(num)

def gen_data_cons():
# Só possui validação de dias 31 ou 30 de meses
    ano = rd.randint(2010,2022)
    mes = rd.randint(1,12)

    if mes % 2 == 0:
        if mes == 2:
            dia_fim = 28
        else:
            dia_fim = 30
    else:
        dia_fim = 31

    dia = rd.randrange(1,dia_fim)
    return str(ano) + '-' + str(mes) + '-' + (2 - len(str(dia)))*'0' + str(dia)
   

def gen_data_nasc():
    # Só possui validação de dias 31 ou 30 de meses
    ano = rd.randint(1930,2022)
    mes = rd.randint(1,12)

    if mes % 2 == 0:
        if mes == 2:
            dia_fim = 28
        else:
            dia_fim = 30
    else:
        dia_fim = 31

    dia = rd.randrange(1,dia_fim)
    return str(ano) + '-' + str(mes) + '-' + (2 - len(str(dia)))*'0' + str(dia)

def gen_cns():
    num = rd.randrange(1,10**15)
    return str(num) + (15 - len(str(num)))*'0'

def gen_nome_equipe():
    return 'Equipe UBS' + ' ' + gen_nome()

def gen_nome_especialidade():
    lista_esp = ['Urologia', 'Neurologia', 'Psiquiatria', 'Pediatria', 'Oncologia', 'Nutrologia', 'Cirurgião Geral']
    return lista_esp[rd.randint(0, len(lista_esp) - 1)]

def gen_cfm_cfo():
    num = rd.randrange(1,10**10)
    return str(num) + (10 - len(str(num)))*'0'

def gen_nome_fabricante():
    nome = names.get_last_name()
    emp = ['Indústrias', 'Farmacéutica']
    return nome + ' ' + emp[rd.randint(0, len(emp) - 1)]

def gen_nome_med():
    nome = names.get_last_name()[:3] + names.get_last_name()[:3].lower()
    return nome
