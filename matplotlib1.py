import matplotlib.pyplot as plt
import numpy as np
a,b,c=np.loadtxt('C:/Users/Yogesh Tripathi/Desktop/pandas1_data.csv',unpack=True,delimiter=',')
plt.plot(a,'gs')
plt.title('Pandas Data')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
