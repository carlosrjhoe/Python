def familia(*nomes):
    for nome in nomes:
        print(f'{nome.title()}')

familia('carlos', 'mayara', 'neto', 'luna', 'rose', 'lucia', 'milena', 'emilly')

print('#'*50)

def perfil_construcao(primeiro, segundo, **informacao_usuario):
    perfil = {}
    perfil['primeiro_nome'] = primeiro
    perfil['segundo_nome'] = segundo
    for k, v in informacao_usuario.items():
        perfil[k] = v.title()
    return perfil
    
    
perfil_princial = perfil_construcao("carlos", "roberto", localizacao="brasil", campo="gilene_di_carle")

print(perfil_princial)