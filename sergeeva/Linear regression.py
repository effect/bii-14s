import numpy as np
import scipy as sc
import matplotlib.pyplot as pl
from sklearn.utils import shuffle
from sklearn import linear_model

# Generate data
x = np.linspace(10, 30, 1000)
y = 0.75 * x + 1.35

# Add noise
noise = np.random.normal(0,0.5, y.size)
y_noise = y + noise * 5

# Make plot with noise
pl.plot(x, y_noise, ',')
pl.plot(x, y, 'k--', label ='Input')
pl.legend(loc='best')


# Train and test sets
x = x.reshape((x.shape[0],-1))
x, y_noise = shuffle(x, y_noise, random_state=1)
x_train = x[:600]
x_test = x[600:]
y_train = y_noise[:600]
y_test = y_noise[600:]

print x_test.shape

# Linear regression
regr = linear_model.LinearRegression()
regr.fit(x_train, y_train)

print 'Coefficients: ', regr.coef_, regr.intercept_
print "Residual sum of squares, train: ", np.mean((regr.predict(x_train) - y_train) ** 2)
print "Residual sum of squares, test: ", np.mean((regr.predict(x_test) - y_test) ** 2)
print 'R^2:', regr.score(x,y_noise)


# Plot linear regression
pl.scatter(x_train, y_train,  color='grey', label='Train')
pl.scatter(x_test, y_test,  color='red', label='Test')
pl.plot(x_test, regr.predict(x_test),'b-', label='Predict')
y = 0.75 * x + 1.35
pl.plot(x, y, 'k--', label='Input')
pl.xlabel('X')
pl.ylabel('Y')
pl.legend(loc='best')


# Second plot (to be continued...)
pl.scatter(x, y_noise,  color='grey')
pl.plot(x_test, regr.predict(x_test),'b-', label='Predict')
pl.legend(loc='best')



