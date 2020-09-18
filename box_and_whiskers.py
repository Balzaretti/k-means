import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

f, ax = plt.subplots(figsize=(7, 6))
names = ['sepal_length','sepal_width','petal_length','petal_width','flower_name']
iris = pd.read_csv('./iris.data', names=names)
sns.boxplot(x="petal_width", y="flower_name", data=iris, whis=[0, 100], width=0.6, palette="vlag")
ax.xaxis.grid(True)
ax.set(ylabel="")
sns.despine(trim=True, left=True)
plt.show()
