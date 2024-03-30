import pandas as pd
pd.options.display.float_format = '{:.2f}'.format

df_Principal = pd.read_excel('acoes_pura.xlsx', sheet_name='Principal')
df_Total_de_acoes = pd.read_excel('acoes_pura.xlsx', sheet_name='Total_de_acoes')

# Ativo	Data	Último (R$)	Var. Dia (%)

df_Principal = df_Principal[['Ativo', 'Data', 'Último (R$)', 'Var. Dia (%)']].copy()

df_Principal = df_Principal.rename(columns={'Último (R$)': 'valor_final', 'Var. Dia (%)': 'var_dia_pct'}).copy()

df_Principal['Var_pct'] = df_Principal['var_dia_pct'] / 100

df_Principal['valor_inicial'] = df_Principal['valor_final'] / (df_Principal['Var_pct'] + 1)

df_Principal = df_Principal.merge(df_Total_de_acoes, left_on='Ativo', right_on='Código', how='left')

df_Principal['variacao_rs'] = (df_Principal['valor_final'] - df_Principal['valor_inicial']) * df_Principal['Qtde. Teórica']

df_Principal['status'] = df_Principal['variacao_rs'].apply(lambda x: 'Subiu' if x > 0 else ('Desceu' if x < 0 else 'Estavel'))

df_Principal['Qtde. Teórica'] = df_Principal['Qtde. Teórica'].astype(int)

df_Principal = df_Principal.rename(columns={'Qtde. Teórica': 'Qtd_teorica'}).copy()

df_Principal = df_Principal.rename(columns={'Seguimentos': 'Segmentos'}).copy()

# df_Principal = df_Principal.drop(columns=['Código'])


# Calculando os valores agregados
maior_valor = df_Principal['variacao_rs'].max()
menor_valor = df_Principal['variacao_rs'].min()
media_valor = df_Principal['variacao_rs'].mean()

# Calculando as médias condicionais
df_Principal_subiu = df_Principal[df_Principal['status'] == 'Subiu']
df_Principal_desceu = df_Principal[df_Principal['status'] == 'Desceu']['variacao_rs'].mean()

# Calculando as médias condicionais
# df_analise_seguimento = df_Principal_subiu.groupby('Seguimento')['variacao_rs'].sum().reset_index()

# Para encontrar os nomes associados ao maior e menor valor, você pode fazer:
# nome_maior = df_Principal.loc[df_Principal['variacao_rs'].idxmax(), 'NomeDaColunaComNomes']
# nome_menor = df_Principal.loc[df_Principal['variacao_rs'].idxmin(), 'NomeDaColunaComNomes']

def informacoes():
    print(f'Maior valor | R$ {maior_valor:,.2f}')
    print(f'Menor valor | R$ {menor_valor:,.2f}')
    print(f'Média | R$ {media_valor:,.2f}')
    # print(f'Média de quem Subiu  R$ {df_Principal_subiu:,.2f}')
    # print(f'Média de quem Desceu  R$ {df_Principal_desceu:,.2f}')
    # print(f'Nome do maior Ativo: {nome_maior}')
    # print(f'Nome do menor Ativo: {nome_menor}')
    
"""



# Para calcular a variação dos que subiram por segmento, você pode agrupar e filtrar:
var_subiu_segmento = df[df['Resultado'] == 'Subiu'].groupby('Segmento')['Variacao_rs'].sum()

# Para adicionar esses valores ao DataFrame, você pode fazer:
df['Variação dos que subiram'] = df.apply(lambda x: var_subiu_segmento[x['Segmento']] if x['Resultado'] == 'Subiu' else 0, axis=1)    
"""


if __name__ == "__main__":
    print(df_analise_seguimento)
    # df_analise_seguimento
    # informacoes()