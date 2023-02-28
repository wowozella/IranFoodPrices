# first line is reserved

import numpy as np
import pandas as pd

My_series = pd.Series(data = np.random.randint(1, 10, 4), index = 'A B C D'.split(), dtype = 'int8')
print(My_series)

df = pd.DataFrame(data = np.random.randn(5,4),
                  index = '1 2 3 4 5'.split(),
                  columns = 'W X Y Z'.split())
print(df)

My_data = pd.read_csv('Iran_food_prices.csv')
