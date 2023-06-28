"""30 - Como criar um DataFrame a partir de um dicionário de listas?"""

import pandas as pd

data = {
    'A': [1,2,3],
    'B': [4,5,6],
    'C': [7,8,9]
}

df = pd.DataFrame(data)
print(df)