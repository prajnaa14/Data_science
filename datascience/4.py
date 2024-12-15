import numpy as np
def initial_centroid(data,k):
    index=np.random.choice(len(data),size=k,replace=False)
    return data[index]

def assign_cluster(data,centroid):
    clusters=[[] for _ in range(len(centroid))]
    for point in data:
        distance=np.linalg.norm(point-centroid, axis=1)
        close_cluster=np.argmin(distance)
        clusters[close_cluster].append(point)
    return clusters

def update_centroid(clusters):
    new_centroids=[]
    for cluster in clusters:
        if cluster:
            new_centroids.append(np.mean(cluster,axis=0))
    return np.array(new_centroids)

def kmeans(data,k,max_itr=100):
    centroids= initial_centroid(data,k)
    for _ in range(max_itr):
        clusters=assign_cluster(data,centroids)
        new_centroid= update_centroid(clusters)
        if np.allclose(centroids,new_centroid,atol=1e-6):
            break
        centroids=new_centroid
    return centroids,clusters

if __name__=="__main__":
    np.random.seed(42)
    data=np.random.rand(100,2)
    k=3
    centroid,cluster=kmeans(data,k)
    print(f"Centroid: {centroid}")
    for i,cluster in enumerate(cluster):
        print(f"cluster {i} : {len(cluster)} points")
