import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Bestsellers with categories.csv')

data.head(5)
data.isnull().sum()
print(data.isnull().sum())

data = data.dropna(subset=['Price', 'User Rating'])

print("Price 10th percentile:", np.quantile(data['Price'], 0.10))

for column in ['Price', 'User Rating']:
    q1, q2, q3 = np.quantile(data[column], [0.25, 0.50, 0.75])
    
    print(f"\n{column}: Q1={q1}, Q2={q2}, Q3={q3}, IQR={q3-q1}")

plt.boxplot([data['Price'], data['User Rating']])
plt.xticks([1, 2], ['Price', 'User Rating'])
plt.show()