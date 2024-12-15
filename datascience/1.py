import matplotlib.pyplot as plt

hours=[10,9,2,15,10,16,11,16]
score=[95,80,10,50,45,98,38,93]

plt.figure(figsize=(10,5))
plt.xlabel("hours")
plt.ylabel("score")
plt.title("effect pf study hours on marks")
plt.grid(True)
plt.plot(hours,score,'r*',markersize=10,linestyle="-")
plt.show()