qtd_pessoas = []
classi_idade = ''
def verificar_idade():
    while True:
        idade = int(input('Informe a idade: '))
        opcao = input('Deseja continuar[S/N]? ').upper()
        qtd_pessoas.append(idade)
        if opcao == 'N':
            break
        else:
            continue

def verificar_media_idade():
    media = sum(qtd_pessoas) / len(qtd_pessoas)
    return media

def classificarcao_idade():
    if verificar_media_idade() <= 25:
        classi_idade = 'Jovem'
    elif verificar_media_idade() >= 26 and verificar_media_idade() <= 60:
        classi_idade = 'Adulta'
    else:
        classi_idade = 'Idosa'
    return classi_idade

def resulmo():
    print(f'Quantidade de pessoas:\t{len(qtd_pessoas)}')
    print(f'Média de idade:\t{verificar_media_idade()}')
    print(f'Classificação da turma:\t{classificarcao_idade()}')
    
if __name__ == "__main__":
    verificar_idade()
    resulmo()