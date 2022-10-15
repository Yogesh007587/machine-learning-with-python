import pandas as p
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

#gathering of data
data=p.read_csv('C:\\Users\\YOGESH TRIPATHI\\Desktop\\pandas1_data.csv')
Y=np.array(data['price'])
X=np.array(data['lotsize'])

X=X.reshape(len(X),1)
Y=Y.reshape(len(Y),1)

#preparing/splitting the data
X_train=X[:-250]
X_test=X[-250:]
Y_train=Y[:-250]
Y_test=Y[-250:]

regr=linear_model.LinearRegression()
regr.fit(X_train,Y_train)

plt.scatter(X_test,Y_test,color='green')
plt.plot(X_test,regr.predict)
plt.title('Test Data')
plt.xlabel('size')
plt.ylabel('Price')
plt.show()


