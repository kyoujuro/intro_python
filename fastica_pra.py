import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import FastICA
import japanize_matplotlib

# サンプルデータの生成
np.random.seed(123)
n_samples = 1000
time = np.linspace(0, 5, n_samples)

s1 = np.sin(2 * time)  
s2 = np.sign(np.sin(3 * time))  
s3 = np.random.normal(size=n_samples) 

S = np.c_[s1, s2, s3]
S += 0.2 * np.random.normal(size=S.shape)  
S /= S.std(axis=0) 


A = np.array([[1, 1, 1], [0.5, 2, 1.0], [2.5, 2.0, 3.0]])  
X = np.dot(S, A.T)  


ica = FastICA(n_components=3)
S_ = ica.fit_transform(X)  # 推定された独立成分
A_ = ica.mixing_  # 推定された混合行列

# 結果のプロット
plt.figure()

models = [X, S, S_]
names = ['観測信号', '元の信号', 'ICAによる推定信号']
colors = ['red', 'blue', 'green']

for i, (model, name) in enumerate(zip(models, names), 1):
    plt.subplot(3, 1, i)
    plt.title(name)
    for sig, color in zip(model.T, colors):
        plt.plot(sig, color=color)

plt.tight_layout()
plt.show()
