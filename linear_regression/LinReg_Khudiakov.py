import numpy as np
import scipy as sc
import scipy.stats as stats
import matplotlib.pyplot as plt
import math
from math import sqrt
import sklearn
from sklearn import linear_model
regr = linear_model.LinearRegression()
import scipy.stats as stats
import statsmodels.api as sm

x = np.linspace(0, 1000, 1000)
y = 15 * x + 10000

noise = np.random.normal(0, 10000, 1000)
y_noise = y + noise

X_train1 = []
X_test1 = []
y_train1 = []
y_test1 = []
for i in range(len(x)):
    if i%2 == 0:
        X_train1.append(x[i])
        y_train1.append(y_noise[i])
    else:
        X_test1.append(x[i])
        y_test1.append(y_noise[i])
X_train=np.asarray(X_train1)
X_test=np.asarray(X_test1)
y_train=np.asarray(y_train1)
y_test=np.asarray(y_test1)
X_train = X_train.reshape(X_train.size, 1)
X_test = X_test.reshape(X_test.size, 1)

regr.fit(X_train, y_train)
print 'Regression coeff for train', regr.coef_[0]
print 'Regression intercept for train', regr.intercept_
regr.fit(X_test, y_test)
print 'Regression coeff for test', regr.coef_[0]
print 'Regression intercept for test', regr.intercept_
print "Training error: ", np.mean((regr.predict(X_train) - y_train) ** 2)
print "Test error: ", np.mean((regr.predict(X_test) - y_test) ** 2)

slope, intercept, r_value, p_value, std_err = stats.linregress(X_train1,y_train1)
line_train = slope * X_train + intercept
err_train=sqrt(np.sum((line_train - y_train1)**2)/len(y_train1))
print 'RSS train', err_train

slope, intercept, r_value, p_value, std_err = stats.linregress(X_test1,y_test1)
line_test = slope * X_test + intercept
err_test=sqrt(np.sum((line_test - y_test1)**2)/len(y_test1))
print 'RSS test', err_test

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y_noise)
print 'r value', r_value
print 'R2 value', r_value ** 2

line_total = slope * x + intercept
err_total = sqrt(np.sum((line_total - y_noise)**2)/len(y_noise))
print'RSS total', err_total

result = sm.OLS(y_noise, x).fit()
N = result.nobs
P = result.df_model
dfn, dfd = P, N - P - 1
F = result.mse_model / result.mse_resid
p = 1.0 - stats.f.cdf(F,dfn,dfd)
print 'F-statistic: {:.3f},  p-value (95% confidence interval): {}'.format( F, p )

plt.plot(X_train, y_train, '.', color='blue', label="training set")
plt.plot(X_test, y_test, '.', color='green', label="test set")
plt.plot(x, y, '-', color='yellow', linewidth=2, label='original line')
plt.plot(X_test, regr.predict(X_test), '-', color = 'red', linewidth = 2, label = 'predicted line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
plt.show()

plt.plot(x, y_noise, '.', color='blue', label="values")
x_arr = np.asarray(x)
x_arr = x.reshape(x.size, 1)
count = 0
for i in range (len(y_noise)):
    if (regr.predict(x[i]) - y_noise[i])**2 < (err_total)**2:
        if count == 0:
            plt.plot(x[i], y_noise[i], '*', color = 'yellow', marker='o', label = 'values within RSS')
            count = 1
        else:
            plt.plot(x[i], y_noise[i], '*', color = 'yellow', marker='o')
plt.plot(x_arr, regr.predict(x_arr), '-', color = 'red', linewidth = 2, label = 'predicted line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
plt.show()