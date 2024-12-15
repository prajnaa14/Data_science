import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris=load_iris()
x=iris.data

def map(data):
    return {
        'sepal_length':data[0],
        'sepal_width':data[1],
        'petal_length':data[2],
        'petal_width':data[3]
    }

def reduce(results):
    stats={}
    for feature in['sepal_length', 'sepal_width','petal_length','petal_width']:
        values=[result[feature] for result in results]
        stats[feature]={
            'min':np.min(values),
            'max':np.max(values),
            'mean':np.mean(values) 
        }
    return stats

mapped=[map(data) for data in x]
min_max=reduce(mapped)
for feature,values in min_max.items():
    print(f"{feature}: 'min':{values['min']}, 'max':{values['max']}, 'mean':{values['mean']}\n")

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.scatter(x[:,0],x[:,1],c='blue',label='iris_data')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.title('sepal length vs sepal width')
plt.grid(True)
plt.legend()

plt.subplot(1,2,2)
plt.scatter(x[:,2],x[:,3],c='red',label='iris_data')
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.title('petal length vs petal width')
plt.grid(True)
plt.legend()
plt.show()