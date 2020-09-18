# k-means
Repositorio k-means

Para esta clase TC1002S se nos pidio hacer una función que nos permita usar KMeans para poder hacer Clusterings. Hicimos las pruebas principales con los datos de iris.data. 

Creemos que estos centros si pueden llegar a ser representativos de los datos ya que se utilizó K-means para encontrar los patrones en los datos. K-means es un algoritmo de clustering  un tipo de lenguaje no supervisado fundamentado en los conceptos de Lazy Learning. Lo anterior significa que nos basamos en un algoritmo que tiene cómo objetivo identificar grupos/categorías dentro de los datos proporcionados (datos que tienen características similares). Un principio que sigue este algoritmo es que define lo que es un dato basado en lo que parece. Para hacer los grupos se debe diferenciar ciertas características que existen entre el conjunto de datos y se apoya principalmente en el hecho de que  cómo en cualquier cálculo, puede haber un error. Conociendo las diferencias se pueden clasificar nuevos objetos dependiendo en qué tan parecidos son a otros y se define una métrica para estimar la similitud entre los objetos o la distancia entre los puntos.
En este caso se obtuvo el valor de k=3  ya que en la base de datos que utilizamos (iris.data) existen tres grupos diferentes: Iris-setosa, Iris-versicolor y Iris-virginica.
Esto lo pudimos observar tanto directa como indirectamente. Pudimos abrir el archivo y contar los valores individuales de estilos de flor que había, y también utilizamos la función describe() que permitió ver la cuenta de cuántos estilos de flor había. 
Si el dataset a trabajar contiene una gran cantidad de variables un valor alto de k nos sería más útil, ya que permitiría agrupar de mejor manera todas estas variables, por el contrario, si nuestro dataset es de pocas variables, nos es más eficiente usar un valor de k menor y así tendríamos un adecuado manejo de los datos. En nuestro caso, como estamos usando un dataset con muy pocas variables, no sería contraproducente elevar el valor de k, ya que nos daría clusters extra que probablemente son de la misma clase. 
Generalmente, los centros de los clusters tienen una separación consistente, y ninguno está súper pegado a los otros. Mantienen cierta distancia.

![](https://github.com/Balzaretti/k-means/blob/master/images/kmeans_out/kmeans_Result.png)


Lo que podemos observar gracias a esto es que las flores no son tan parecidas entre ellas. Esto significa que algunas flores son más grandes que otras, tales sea por el tamaño de sus pétalos o de sus sépalos. Aunque hay “outliers”, es decir, flores más grandes o pequeñas, los centros dictaminan el promedio, y por tanto se puede deducir que algunas flores son más grandes o pequeñas.

Al graficar en diagramas de caja y bigotes, podemos observar que hay muchos outliers.

![](https://github.com/Balzaretti/k-means/blob/master/Box_and_Whiskers/petal_length.png)
![](https://github.com/Balzaretti/k-means/blob/master/Box_and_Whiskers/sepal_width.png)
![](https://github.com/Balzaretti/k-means/blob/master/Box_and_Whiskers/petal_length.png)
![](https://github.com/Balzaretti/k-means/blob/master/Box_and_Whiskers/petal_width.png)

Como podemos ver, hay bastantes outliers, especialmente entre iris versicolor e iris virginica, que son flores de tamaños similares. Debido a esto, se tiene que tener mucho cuidado con que alguna flor esté metida en la rama equivocada. Sin embargo, debido a que el promedio es reducido, y considera mucho más valores, podemos estar muy seguros de que los centros son los correctos.

Para poder observar los acumulativos en tamaños, utilizamos histogramas. Gráficas a continuación.

![](https://github.com/Balzaretti/k-means/blob/master/Histograms/sepal_length.png)
![](https://github.com/Balzaretti/k-means/blob/master/Histograms/sepal_width.png)
![](https://github.com/Balzaretti/k-means/blob/master/Histograms/petal_length.png)
![](https://github.com/Balzaretti/k-means/blob/master/Histograms/petal_width.png)
