import random
from random import seed
import pandas as pd

seed(1)

export_path = 'randoms.csv'
min = 1979
max = 2561
n = max - min
values = []


for _ in range(n):
    r = random.randint(min, max) 
    values.append(r)

df = pd.DataFrame(values, columns=['random'])
df.to_csv(export_path)

