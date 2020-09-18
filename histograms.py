#Nos permite usar hist() y graficar la funcion
import matplotlib.pyplot as plt
#Leer el archivo
import pandas as pd

#Headers para las columnas
names = ['sepal_length','sepal_width','petal_length','petal_width','flower_name']
#Leer el archivo
iris = pd.read_csv('./iris.data', names=names)

#genera un histograma, con nombre en eje x, y lo muestra
plt.hist(iris['petal_width'], color='g')
plt.xlabel('petal_width')
plt.show()
