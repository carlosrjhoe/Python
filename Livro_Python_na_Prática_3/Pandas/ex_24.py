"""24 - Como criar uma Serie Pandas a partir de uma lista?"""

import pandas as pd

data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,]
s = pd.Series(data)
print(s)