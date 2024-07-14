import pandas as pd
import prince
import matplotlib.pyplot as plt

respondent = ['A', 'B', 'C', 'D', 'E']
q1 = ['Yes', 'No', 'Yes', 'Yes', 'No']
q2 = ['No', 'Yes', 'Yes', 'No', 'Yes']
q3 = ['Yes', 'Yes', 'No', 'No', 'Yes']


df = pd.DataFrame({
    'Question1': q1,
    'Question2': q2,
    'Question3': q3
}, index=respondent)
df = df.replace({'Yes': 1, 'No': 0})

ca = prince.CA(n_components=2)
ca = ca.fit(df)
coordinates = ca.row_coordinates(df)


fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(coordinates.iloc[:, 0], coordinates.iloc[:, 1])


for i, txt in enumerate(coordinates.index):
    ax.annotate(txt, (coordinates.iloc[i, 0], coordinates.iloc[i, 1]))
ax.axhline(0, color='black')
ax.axvline(0, color='black')
plt.show()

