"""25 - Como criar uma Serie a partir de uma array do tipo Numpy?"""

import pandas as pd
import numpy as np

data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
s = pd.Series(data)
print(s)