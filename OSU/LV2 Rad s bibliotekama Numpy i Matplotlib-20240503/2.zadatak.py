import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('LV2 Rad s bibliotekama Numpy i Matplotlib-20240503\data.csv', delimiter=",", dtype="str")
data = data[1::]
data = np.array(data,np.float64)
print(len(data))
height = data[:,1]
weight = data[:,2]
plt.scatter(height,weight)
plt.show()
height = data[::50,1]
weight = data[::50,2]
plt.scatter(height,weight)
plt.show()
print(f"max: {height.max()} min:  {height.min()} mean: {height.mean()}")

men = data[data[:,0]==1]
women = data[data[:,0]==0]
menHeight = men[:,1]
menWeight = men[:,2]
womenHeight = women[:,1]
womenWeight = women[:,2]
plt.scatter(menHeight,menWeight,color = 'blue')
plt.scatter(womenHeight,womenWeight,color = 'red')
plt.show()
