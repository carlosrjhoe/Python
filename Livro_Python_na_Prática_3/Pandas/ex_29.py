"""29 - Como criar um DataFrame a partir de uma lista Python?"""

import pandas as pd

data = [[1,2,3], [4,5,6], [7,8,9]]
df = pd.DataFrame(data, columns = ['A', 'B', 'C'])
print(df)

# >>>    A  B  C
# >>> 0  1  2  3
# >>> 1  4  5  6
# >>> 2  7  8  9