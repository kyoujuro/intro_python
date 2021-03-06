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

e_x = randn(num_data)
e_y = randn(num_data)
e_z = randn(num_data)

Z = 3.3*e_x + e_z
Y = 3.3*e_x + e_y

np.corrcoef(Z, Y)
# %%
Z_std = scipy.stats.zscore(Z)
Y_std = scipy.stats.zscore(Y)

plt.scatter(Z_std, Y_std)
# %%
num_data = 600
e_x = randn(num_data)
e_y = randn(num_data)

x = e_x
y = e_y

plt.scatter(x, y)
# %%
np.corrcoef(x, y)
# %%
z = x + y

x_new = np.array([])
y_new = np.array([])
# %%

for i in range(num_data):
    if z[i] > 0.0:
        x_new = np.append(x_new, x[i])
        y_new = np.append(y_new, y[i])

plt.scatter(x_new, y_new)
# %%
np.corrcoef(x_new, y_new)
# %%

num_data = 200
x_1 = np.random.randint(15, 76, num_data)

x_2 = np.random.randint(0, 2, num_data)
# %%
from scipy.special import expit # 1.
e_x = randn(num_data)

z_base = x_1 + (1 - x_2)*10 - 40 + 5*e_z

z_prob = expit(0.1 * z_base)
# %%
Z = np.array([])
for i in range(num_data):
    Z_i = np.random.choice(2, size=1, p=[1-z_prob[i], z_prob[i]])[0]
    Z = np.append(Z, Z_i)
# %%
e_y = randn(num_data)
Y = -x_1 + 30*x_2 + 10*Z + 80 + 10*e_y

# %%
import pandas as pd
df = pd.DataFrame({'age':x_1,
                   'Sex':x_2,
                   'WatchedCM':Z,
                   'PurchaseAmount':Y,
                   })
df.head()

# %%
print(df[df["WatchedCM"] == 1.0].mean())
print("-----------")
print(df[df["WatchedCM"] == 0.0].mean())
# %%
from sklearn.linear_model import LinearRegression
X = df[["age","Sex","WatchedCM"]]
y = df["PurchaseAmount"]

reg = LinearRegression().fit(X, y)
print("Coef:", reg.coef_)
# %%
from sklearn.linear_model import LogisticRegression
X = df[["age", "Sex"]]
Z = df["WatchedCM"]

reg = LogisticRegression().fit(X, Z)
print("Coef_beta:", reg.coef_)
print("Coef_alpha:", reg.intercept_)
# %%

Z_pre = reg.predict_proba(X)
print(Z_pre[0:5])
print("-----")
print(Z[0:5])
# %%

ATE_i = Y/Z_pre[:, 1]*Z - Y/Z_pre[:, 0]*(1-Z)
ATE = 1/len(Y)*ATE_i.sum()
print("predicted_ATE", ATE)
# %%
X = df[["age","Sex","WatchedCM"]]
y = df["PurchaseAmount"]

reg2 = LinearRegression().fit(X, y)
X_0 = X.copy()
X_0["WatchedCM"] = 0
Y_0 = reg2.predict(X_0)

X_1 = X.copy()
X_1["WatchedCM"] = 1
Y_1 = reg2.predict(X_1)

X = df[["age", "Sex"]]
Z = df["WatchedCM"]

reg = LogisticRegression().fit(X, Z)
Z_pre = reg.predict_proba(X)
print(Z_pre[0:5])
# %%
ATE_1_i = Y/Z_pre[:, 1]*Z + (1-Z/Z_pre[:, 1])*Y_1
ATE_0_i = Y/Z_pre[:, 0]*(1-Z) + (1-(1-Z)/Z_pre[:, 0])*Y_0
ATE = 1/len(Y)*(ATE_1_i-ATE_0_i).sum()
print("Estimated_ATE",ATE)
# %%

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

X = df[["age", "Sex"]]
Z = df["WatchedCM"]

X_train, X_val, Z_train, Z_val = train_test_split(
    X, Z, train_size = 0.6, random_state = 0)

clf = DecisionTreeClassifier(max_depth=1, random_state=0)
clf.fit(X_train, Z_train)
print("Performance_of_Depth1:",clf.score(X_val, Z_val))
# %%

clf = DecisionTreeClassifier(max_depth=2, random_state=0)
clf.fit(X_train, Z_train)
print("Performance_of_Depth2:",clf.score(X_val, Z_val))

clf = DecisionTreeClassifier(max_depth=3, random_state=0)
clf.fit(X_train, Z_train)
print("Performance_of_Depth3:",clf.score(X_val, Z_val))
# %%


from sklearn.tree import DecisionTreeRegressor
X = df[["age", "Sex"]]
Y = df["PurchaseAmount"]

X_train, X_val, Y_train, Y_val = train_test_split(
    X, Y, train_size = 0.6, random_state = 0)

reg = DecisionTreeRegressor(max_depth=2, random_state=0)
reg.fit(X_train, Y_train)
print("Performance_of_Depth1:",reg.score(X_val, Y_val))

reg = DecisionTreeRegressor(max_depth=3, random_state=0)
reg.fit(X_train, Y_train)
print("Performance_of_Depth2:",reg.score(X_val, Y_val))

reg = DecisionTreeRegressor(max_depth=4, random_state=0)
reg.fit(X_train, Y_train)
print("Performance_of_Depth3:",reg.score(X_val, Y_val))
# %%
from sklearn.ensemble import RandomForestClassifier


X = df[["age", "Sex"]]
Z = df["WatchedCM"]


X_train, X_val, Z_train, Z_val = train_test_split(
    X, Z, train_size = 0.6, random_state = 0)

clf = RandomForestClassifier(max_depth=1, random_state=0)
clf.fit(X_train, Z_train)
print("Performance_of_Depth1:",clf.score(X_val, Z_val))

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(X_train, Z_train)
print("Performance_of_Depth2:",clf.score(X_val, Z_val))

clf = RandomForestClassifier(max_depth=3, random_state=0)
clf.fit(X_train, Z_train)
print("Performance_of_Depth3:",clf.score(X_val, Z_val))
