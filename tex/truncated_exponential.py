import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rng

rng.seed(0)

L = 12.34                   # True value of L
N = 100                     # Number of data points
t_min, t_max = 5.0, 20.0    
t = []
for i in range(0, N):
    while True:
        tt = -L*np.log(rng.rand())
        if tt > t_min and tt < t_max:
            break
    t.append(tt)

plt.hist(t, bins=100, color="k", alpha=0.1)
plt.xlabel("$t$", fontsize=16)
plt.xlim([0.0, 30.0])
plt.ylim([0, 6])
plt.title("Photon Arrival Times")
plt.show()

