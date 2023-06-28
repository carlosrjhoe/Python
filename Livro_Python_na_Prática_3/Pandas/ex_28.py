"""28 - Como criar uma Serie com índice personalizado?"""

import pandas as pd

data = [1,2,3,4,5]
index = ['A', 'B', 'C', 'D', 'E']
S = pd.Series(data, index=index)
print(f'{S}')