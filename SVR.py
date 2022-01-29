import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV

boston = load_boston()
X, Xtest, y, ytest = train_test_split(boston['data'], boston['target'], test_size=0.25)
def generate_crossvalidation():
    m_train = np.floor(len(y)*0.75).astype(int)
    train_indices = np.arange(m_train)
    test_indices = np.arange(m_train, len(y))
    yield (train_indices, test_indices)
scaler = StandardScaler()
X_norm = scaler.fit_transform(X)