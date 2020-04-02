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
                   
