def mostra_msg_maior(string_1, string_2):
    len1 = len(string_1)
    len2 = len(string_2)
    
    if len1 > len2:
        print(f'{string_1} tem {len1} letras, e é a string de maior tamanho.')
    elif len2 > len1:
        print(f'{string_2} {len2} letras e é a string de maior tamanho.')
    else:
        print(f'{len1} e {len2} são strings do mesmo tamanho.')
    
mostra_msg_maior('carlos roberto', 'mayara ramos cordeiro')