#Nos permite usar la funcion boxplot()
import seaborn as sns
#Nos permite graficar
import matplotlib.pyplot as plt
#Usado para leer el archivo .csv
import pandas as pd

#Genera una grafica
f, ax = plt.subplots(figsize=(7, 6))
#Nombramos las columnas para separarlas
names = ['sepal_length','sepal_width','petal_length','petal_width','flower_name']
#Leemos el archivo
iris = pd.read_csv('./iris.data', names=names)
#generamos la caja y bigotes
sns.boxplot(x="petal_width", y="flower_name", data=iris, whis=[0, 100], width=0.6, palette="vlag")
#Shows a grid en la sección x
ax.xaxis.grid(True)
#Evita que el eje y tenga nombres
ax.set(ylabel="")
#Hace que la grafica se vea ligeramente mejor
sns.despine(trim=True, left=True)
#Muestra la grafica
plt.show()
