from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans, BisectingKMeans
from pyspark.ml.evaluation import ClusteringEvaluator

spark=SparkSession.builder.appName("Clustering").getOrCreate()
dataset=spark.read.format("libsvm").load("C:\\Users\\PRAJNA\\Downloads\\Big_Data\\datascience\\kmeans_data.txt")

models=[
    (KMeans().setK(2).setSeed(1),"KMeans"),
    (BisectingKMeans().setK(2).setSeed(1),"BisectingKMeans")
]

for model,name in models:
    trained_model=model.fit(dataset)
    predictions=trained_model.transform(dataset)
    silhouette=ClusteringEvaluator().evaluate(predictions)
    predictions.show(truncate=False)
    print(f"{name}silhoutte scre: {silhouette}\n")
    print(f"{name} cluster center: {trained_model.clusterCenters()}")

spark.stop()