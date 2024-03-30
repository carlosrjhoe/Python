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

df_Principal = df_Principal.drop(columns=['Código'])


if __name__ == "__main__":
    print(df_Principal)