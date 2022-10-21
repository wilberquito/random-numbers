import random
from random import seed

seed(1)

min = 1979
max = 2561
n = max - min

for _ in range(n):
    r = random.randint(min, max) 
    print(r)

