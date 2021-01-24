#%%
import random
import numpy as np
from numpy.random import randn
num_data  = 200
e_z = randn(num_data)
e_y = randn(num_data)

Z = e_z
Y = 2*Z + e_y
# %%
np.corrcoef(Z, Y)

# %%
import scipy.stats
import matplotlib.pyplot as plt
%matplotlib inline
Z_std = scipy.stats.zscore(Z)
Y_std = scipy.stats.zscore(Y)

plt.scatter(Z_std, Y_std)
# %%
e_z = randn(num_data)
e_y = randn(num_data)

Y = e_y
Z = 2*Y + e_z
np.corrcoef(Z, Y)


# %%
Z_std = scipy.stats.zscore(Z)
Y_std = scipy.stats.zscore(Y)

plt.scatter(Z_std, Y_std)
# %%
