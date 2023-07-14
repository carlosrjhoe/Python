"""31 - Como criar um DataFrame a partir de uma Array do tipo Numpy?"""

import pandas as pd
import numpy as np

def data_frame(lista):
    df = pd.DataFrame(lista, columns = ['A', 'B', 'C'])
    print(df)

if __name__ == '__main__':  
    data = np.array([[1,2,3],[4,5,6],[7,8,9]])
    data_frame(data)
    