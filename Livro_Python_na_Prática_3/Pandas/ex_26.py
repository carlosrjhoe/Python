"""26 - Como criar uma Serie a partir de um dicionário Python?"""

import pandas as pd

data = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}

s = pd.Series(data)
print(s)