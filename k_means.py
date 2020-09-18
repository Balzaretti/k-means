import math
import numpy as np
def distancia(lista1, lista2):
    distancia_euclideana=math.dist(lista1, lista2)
    return distancia_euclideana

def cercanos(puntos, centros, k):
    clusters=[]
    i=0
    while i<k:
        clusters.append([])
        i+=1


    for i in puntos:
        distancias=[]
        for j in centros:
            valor=distancia(i, j)
            distancias.append(valor)
        menor=99999999999999
        for n in distancias:
            if(distancias[n]<menor):
                menor=distancias[n]
        clusters[menor].append(puntos[i])
    return clusters

def centros(k_listas):
    nuevos_centros=[]
    arreglos_numpy=[]
    suma=0
    count=0
    for i, cluster in enumerate(k_listas):
        suma=0
        count=0
        for punto in cluster:
            suma+=punto
            count+=1
        promedio=suma/count
        nuevos_centros.append(promedio)
    return nuevos_centros

def k_means(puntos):
    k=int(input("Dame un valor para k:\n"))
    rep=0
    centros=[]
    while rep<k:
        centros.append(puntos[rep])
        rep+=1
    rep=0
    while rep<100:
        centros=centros(puntos)
        cercanos(puntos,centros,k)
    print(centros)
