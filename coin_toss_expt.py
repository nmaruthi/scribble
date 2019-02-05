# Snippet to generate a random coin toss experiment

import numpy as np
np.random.seed(123)
outcomes = []
for x in range(100):
    coin = np.random.randint(0,2)
    if(coin==0):
        outcomes.append("heads")
    else:
        outcomes.append("tails")
print(outcomes)