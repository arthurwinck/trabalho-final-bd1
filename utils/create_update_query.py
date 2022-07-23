def create_update_query(var_dic: dict, table: str, id_column: str, id: int):
    size = len(var_dic)

    lista_valores = list(var_dic.values())
    lista_colunas = list(var_dic.keys())

    new_list_valores = []
    new_list_colunas = []

    for i in range(len(lista_valores)):
        if lista_valores[i] != '':
            new_list_valores.append(lista_valores[i])
            new_list_colunas.append(lista_colunas[i])
            
    string_update = ''

    if size > 1:
        string_update = f"""{new_list_colunas[0]} = {new_list_valores[0]} """ 
        for i in range(1, len(new_list_valores)):
            print(i, new_list_valores[i], type(new_list_valores[i]))
            string_update += f""", {new_list_colunas[i]} = \"{new_list_valores[i]}\" """
                
    query = f"""UPDATE {table} set """ + string_update + f"""WHERE {id_column} = {id}"""

    print(query)

    return query

#print(create_update_query({"nome": "arthur", "idade": 15}, "tb_cidadao", "id", 5))