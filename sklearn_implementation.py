#Permite usar KMeans
from sklearn.cluster import KMeans
#Acepta arreglos de numpy como input
import numpy as np
#leer el archivo
import pandas as pd
#inicializa el "objeto"
kmeans = KMeans(n_clusters=3)
#Nombres para las columnas
names = ['sepal_length','sepal_width','petal_length','petal_width','flower_name']
#Leer el archivo
df=pd.read_csv('./iris.data', names=names)
#Borrar columna de texto
del df['flower_name']
#convertir a arreglo de numpy
data=np.asarray(df)
#utiliza Kmeans
kmeans.fit(data)
#imprime los valores
print(kmeans.cluster_centers_)
