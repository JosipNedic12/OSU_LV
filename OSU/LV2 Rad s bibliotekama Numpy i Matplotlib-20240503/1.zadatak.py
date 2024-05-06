import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 3, 1]) 
y = np.array([1, 2, 2, 1, 1])
plt.plot(x,y,'b', linewidth=2, marker='.', markersize=10)
plt.axis([0, 4.0, 0, 4.0])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Slika 2.3')
plt.show()