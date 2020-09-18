from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
kmeans = KMeans(n_clusters=3)
names = ['sepal_length','sepal_width','petal_length','petal_width','flower_name']
df=pd.read_csv('./iris.data', names=names)
del df['flower_name']
data=np.asarray(df)
kmeans.fit(data)

print(kmeans.cluster_centers_)
