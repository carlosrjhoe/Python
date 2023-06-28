"""27 - Como criar uma Serie a partir de uma Tupla Nomeada?"""

import pandas as pd
from collections import namedtuple

Data = namedtuple('Data', ['A', 'B', 'C', 'D', 'E', 'F'])
data = Data(1, 2, 3, 4, 5, 6)
d = pd.Series(data)
print(d)