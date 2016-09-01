import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rng

rng.seed(0)

# GENERATE A DATASET

L = 47.34                   # True value of L
N = 5                       # Number of data points
t_min, t_max = 5.0, 20.0    
t = []
for i in range(0, N):
    while True:
        tt = -L*np.log(rng.rand())
        if tt > t_min and tt < t_max:
            break
    t.append(tt)

t = np.array(t)

plt.hist(t, bins=100, color="k", alpha=0.1)
plt.xlabel("$t$", fontsize=16)
plt.xlim([0.0, 30.0])
plt.ylim([0, 3])
plt.title("Photon Arrival Times")
plt.show()

# TO INFER L from {t}, need the likelihood. Here it is.
# Not using log-likelihood, because N isn't too big.
L = np.linspace(0.0, 1000.0, 10001)
likelihood = L**(-N)\
                *(np.exp(-t_min/L) - np.exp(-t_max/L))\
                *np.exp(-t.sum()/L)

plt.plot(L, likelihood, "k")
plt.xlabel("$L$", fontsize=16)
plt.ylabel("Likelihood")
plt.title("Spot the problem...")
plt.show()

