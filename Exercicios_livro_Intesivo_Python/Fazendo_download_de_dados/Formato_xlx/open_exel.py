import pandas as pd

df = pd.read_excel(r'Fazendo_download_de_dados\Formato_xlx\Planilha_de_manutenção_Ache.xlsx')

cont = 0

# if df['Empregado'] == 'CARLOS ROBERTO':
#     cont += 1
# print(cont)
    

print(f"{df['Empregado']} - {df['Hora iníc.real']} - {df['Hora fim real']}")