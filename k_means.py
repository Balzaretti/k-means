import math
def distancia(lista1, lista2):
    distancia_euclideana=math.dist(lista1, lista2)
    return distancia_euclideana

lista1=[4,5]
lista2=[6,7]
print(distancia(lista1,lista2))
