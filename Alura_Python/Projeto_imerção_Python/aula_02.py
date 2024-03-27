import pandas as pd

if __name__ == "__main__":
    df_ChatGPT = pd.read_excel('acoes_pura.xlsx', sheet_name='ChatGPT')
    print(df_ChatGPT)