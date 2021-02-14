import numpy as np

def pca(X, n_components=2):
    X = X - X.mean(axis=0)
    cov = np.cov(X, rowvar=False)
    l, v = np.linalg.eig(cov)
    l_index = np.argsort(l)[::-1]
    v_ = v[:, l_index]

    components = v_[:,:n_components]
    T = np.dot(X, components)
    return T
    
