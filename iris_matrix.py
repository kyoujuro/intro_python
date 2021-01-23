from sklearn.datasets import load_iris
from IPython.display import display
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

iris_data = load_iris()
iris_df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
iris_df["target"] = iris_data.target

display(iris_df.head())
display(iris_df.tail())

display(iris_df.describe())
from sklearn.decomposition import PCA
import numpy as np

x_train, x_test, y_train, y_test = train_test_split(
    iris_df.iloc[:, 0:4],
    iris_df.iloc[:, 4],
    test_size = 0.3,
    random_state = 1
)

scl = StandardScaler()
scl.fit(x_train)
x_train_std = scl.transform(x_train)
x_test_std = scl.transform(x_test)
pca = PCA()
pca.fit(x_train_std)

tot = sum(pca.explained_variance_ratio_)
print("寄与率:", str(["{:.1f}%".format(val * 100/tot) for val in 
                   pca.explained_variance_ratio_]))
                   
# sklearnのFactorAnalysis(因子分析)クラスをインポート
from sklearn.decomposition import FactorAnalysis as FA

# 因子数を指定
n_components=3

# 因子分析の実行
fa = FA(n_components, max_iter=5000) # モデルを定義
fitted = fa.fit_transform(z) # fitとtransformを一括処理

print(fitted)
print(fitted.shape)

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
sns.set_style('whitegrid')

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
# %%
def generate_sample_data(num, seed=0):
    target_list = [] # 目的変数のリスト
    feature_vector_list = [] # 説明変数（特徴量）のリスト

    feature_num = 10 # 特徴量の数
    intercept = 0.2 # 切片
    weight = [0.2, 0.3, 0.5, -0.4, 0.1, 0.2, 0.5, -0.3, 0.6, 0.9] # 各特徴量の重み

    np.random.seed(seed=seed)
    for i in range(num):
        feature_vector = [np.random.rand() for n in range(feature_num)] # 特徴量をランダムに生成
        noise = [np.random.normal(0, 0.1) for n in range(feature_num)] # ノイズをランダムに生成
        target = sum([intercept+feature_vector[n]*weight[n]+noise[n] for n in range(feature_num)]) # 目的変数を生成

        target_list.append(target)
        feature_vector_list.append(feature_vector)

    df = pd.DataFrame(np.c_[target_list, feature_vector_list], 
                      columns=['target', 'feature0', 'feature1', 'feature2', 
                               'feature3', 'feature4', 'feature5', 'feature6', 'feature7','feature8','feature9'])
    return df

data = generate_sample_data(num=1000, seed=0)

X = data.drop('target', axis=1)
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# %%
import pystan
import arviz
# %%
sample_code = """
    data {
        int<lower=0> N;
        int<lower=0> D;
        matrix[N, D] X;
        vector[N] y;
        int<lower=0> N_new;
        matrix[N_new, D] X_new;
    }
    parameters {
        real w0;
        vector[D] w;
        real<lower=0> sigma;
    }
    model {
        for (i in 1:N)
            y[i] ~ normal(w0 + dot_product(X[i], w), sigma);
    }
    generated quantities {
        vector[N_new] y_new;
        for (i in 1:N_new)
            y_new[i] = normal_rng(w0 + dot_product(X_new[i], w), sigma);
    }
"""

sample_data = {
    'N': X_train.shape[0],
    'D': X_train.shape[1],
    'X': X_train,
    'y': y_train,
    'N_new': X_test.shape[0],
    'X_new': X_test
}
# %%
sm = pystan.StanModel(model_code=sample_code)
# %%
fit = sm.sampling(data=sample_data, iter=1000, chains=4)
print(fit)
# %%
arviz.plot_trace(fit)
plt.show()
# %%
