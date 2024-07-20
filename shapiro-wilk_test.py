import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns


data = np.random.normal(loc=0, scale=1, size=10_000)
stat, p_value = stats.shapiro(data)
print('Shapiro-Wilk検定の統計量: {:.3f}'.format(stat))
print('p値: {:.3f}'.format(p_value))

if p_value > 0.05:
    print('データは正規分布に従っていると考えられます。')
else:
    print('データは正規分布に従っていないと考えられます。')

sns.histplot(data, kde=True)
plt.title('データのヒストグラムとカーネル密度推定')
plt.xlabel('値')
plt.ylabel('頻度')
plt.show()
