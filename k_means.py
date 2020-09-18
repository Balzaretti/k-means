import math
import numpy as np
def distancia(lista1, lista2):
    distancia_euclideana=math.dist(lista1, lista2)
    return distancia_euclideana

def cercanos(puntos, centros):
    clusters=[[] for k in centros]


    for i, punto in puntos:
        distancias=[]
        for j, centro in centros:
            valor=distancia(punto, centro)
            distancias.append(valor)
        menor=99999999999999
        for n in distancias:
            if(distancias[n]<menor):
                menor=distancias[n]
        clusters[menor].append(punto)
    return clusters

def centros(clusters):
    nuevos_centros=[]
    for cluster in clusters:
        nuevos_centros.append(np.mean(cluster, axis=0))
    return nuevos_centros

def k_means(puntos):
    k=int(input("Dame un valor para clusters:\n"))
    idx = np.random.randint(len(points),size=k)
    centros = points[idx,:]
    clusters = cercanos(puntos,centros)
    iteraciones=int(input("Cuantas iteraciones quieres?\n"))
    for i in range(iteraciones):
        clusters=cercanos(puntos, centros)
        centros=centros(clusters)
    return clusters, centros

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

def main():
    filename = './iris.data'
    data = load_data(filename)
    X=np.array([f[:-1] for f in data])
    y=np.array([f[-1] for f in data])
    clusters, centros = k_means(X)

if __name__=="__main__":
    main()
