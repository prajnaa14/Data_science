import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("C:\\Users\\PRAJNA\Downloads\\Big_Data\\datascience\\mtcars.csv")
plt.figure(figsize=(10,5))
plt.hist(df['mpg'],color='skyblue',bins=10,edgecolor='black')
plt.title("frequency of destrivution of mpg")
plt.xlabel("MPG")
plt.ylabel("frequency")
plt.grid(True)
plt.show()