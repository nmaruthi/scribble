# Coin toss experiment with a plot
import numpy as np
import matplotlib.pyplot as plt

expts=[]
for trails in range(10):
    expt=[1]
    for trial in range(100):
        throw=np.random.randint(1,7)
        if throw<=2:
            step=max(0, expt[-1]-1)
        elif throw<=5:
            step=expt[-1]+1
        else:
            step=expt[-1]+np.random.randint(1,7)
        expt.append(step)
    expts.append(expt)
np_expts=np.array(expts)
print(expts)

plt.plot(expts)

np_expts_t=np.transpose(np_expts)