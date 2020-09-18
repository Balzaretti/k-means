import math
import numpy as np
from visualizations import show_clusters_centroids

def distancia(lista1, lista2):
    #Distancia Euclideana
    return np.sqrt(np.sum((np.array(lista2)-np.array(lista1))**2))

def cercanos(puntos, centros):
    clusters=[[] for k in centros]
    #genera valores de distancias
    for i, punto in enumerate(puntos):
        distancias=[]
        for j, centro in enumerate(centros):
            valor=distancia(punto, centro)
            distancias.append(valor)
        menor=np.argmin(distancias)
        clusters[menor].append(punto)
    return clusters

def centros(clusters):
    nuevos_centros=[]
    #promedios de los centros
    for cluster in clusters:
        nuevos_centros.append(np.mean(cluster, axis=0))
    return nuevos_centros

def k_means(puntos):
    k=int(input("Dame un valor para clusters:\n"))
    #Valores al azar para los centros
    idx = np.random.randint(len(puntos),size=k)
    centroides = puntos[idx,:]
    #Genera clusters iniciales
    clusters = cercanos(puntos,centroides)
    #Permite mas cercania al valor "real"
    iteraciones=int(input("Cuantas iteraciones quieres?\n"))
    for i in range(iteraciones):
        clusters=cercanos(puntos, centroides)
        centroides=centros(clusters)
    return clusters, centroides

def load_data(filename):
    with open(filename,'r') as fp:
        data = fp.read().split('\n')
    data_new = [f.split(',') for f in data if f != ""]
    data_formatted = []
    for instance in data_new:
        instance_new = []
        for value in instance:
            try:
                instance_new.append(float(value))
            except ValueError:
                instance_new.append(value)
        data_formatted.append(instance_new)
    return data_formatted

#Para inicializar la funcion
def main():
    filename = './iris.data'
    data = load_data(filename)
    #consigue todas las columnas, menos la ultima
    X=np.array([f[:-1] for f in data])
    #consigue la ultima columna, de nombres
    y=np.array([f[-1] for f in data])
    #inicializa k_means
    clusters, centros = k_means(X)
    #imprime los valores de los centros, en 4 dimensiones
    print(centros)
    #genera una grafica con los valores finales
    show_clusters_centroids(clusters,centros,"Result", keep=True)
    #muestra la grafica
    plt.show()
if __name__=="__main__":
    main()
