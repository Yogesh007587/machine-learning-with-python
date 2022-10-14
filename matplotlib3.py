import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig=plt.figure()
ax=fig.gca(projection='3d')
x=np.arrange(-5,5,0.25)
y=np.arrange(-5,5,0.25)
x,y=np.meshgrid(x,y)
r=np.sqrt(x**2+y**2)
z=np.sin(r)
surf=ax.plot_surface(x,y,z,rstride=1,cstride=1,cmap=cm.coolwarm)
plt.show()
