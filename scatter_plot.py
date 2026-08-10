import matplotlib.pyplot as plt
import numpy as np
x1points=[3,6,9,12,15]
y1points=[4,8,10,14,16]
x2points=[5,10,15,20,25]
y2points=[6,12,17,20,26]
plt.plot(x1points,y1points, color = 'orange')
plt.scatter(x1points,y1points ,color = 'brown')
plt.scatter(x2points ,y2points,color = 'pink')
plt.show()