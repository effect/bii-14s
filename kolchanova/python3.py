#!/usr/bin/python

import numpy, scipy
from math import sqrt
from scipy import stats
import matplotlib.pyplot as plot
import random
%matplotlib inline

x = numpy.linspace(0, 2, 1000)
y = 2 * x + 1
noise = scipy.randn(y.size)
y_noise = y + noise

X_full = numpy.array(x).T
y_full = numpy.array(y_noise).T
print (X_full.shape)
print (y_full.shape)

TRAIN_SIZE = 800
from sklearn.utils import shuffle
x, y_noise = shuffle(x, y_noise, random_state=1)
x_train = x[:TRAIN_SIZE]
y_train = y_noise[:TRAIN_SIZE]
x_test = x[TRAIN_SIZE:]
y_test = y_noise[TRAIN_SIZE:]

X_train = numpy.asmatrix(x_train).T
Y_train = numpy.asmatrix(y_train).T
Train_set = numpy.hstack((X_train, Y_train))
print (Train_set.shape)

X_test = numpy.asmatrix(x_test).T
Y_test = numpy.asmatrix(y_test).T
Test_set = numpy.hstack((X_test,Y_test))
print (Test_set.shape)

betas = scipy.polyfit(x, y_noise, 1)[::-1]  # 1 is order (max degree of x)
print ("betas:", betas)
print ("original model: y = 2 * x + 1")
print ("proposed model: y = 1.99725967*x + 1.03406303")

_ = plot.plot(x, y_noise, "r.", label = "full set")
_ = plot.plot(x, betas[0] + betas[1]*x, color="blue", label = "model")
plot.xlabel('X')
plot.ylabel('Y')
_ = plot.legend(bbox_to_anchor = (1.05, 1), loc = 2, borderaxespad = 0)

from sklearn import linear_model
regr = linear_model.LinearRegression()
regr.fit(X_train, Y_train)
print(regr.coef_)
print(regr.intercept_)

regr.fit(X_test, Y_test)
print (regr.coef_)
print (regr.intercept_)

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y_noise)
print ("Full set r-squared (determination coefficient):", r_value**2)
print ("standard error = ", std_err)

train_set_error = sqrt(numpy.sum(((slope*x_train+intercept) - y_train)**2)/len(y_train))
print ('Residual sum of squares, train:', train_set_error)

test_set_error = sqrt(numpy.sum(((slope*x_test+intercept) - y_test)**2)/len(y_test))
print ('Residual sum of squares, test:', test_set_error)

from scipy.stats import pearsonr
print ("Correlation coefficient:")
pearsonr(x, y_noise) #correlation coefficient x1

print ("Correlation coefficient array:")
numpy.corrcoef(x,y_noise) #correlation coefficient x2

_ = plot.plot(x_train, y_train, "r.", label = "train")
_ = plot.plot(x_test,y_test, "b.", label  = "test")
_ = plot.plot(x, betas[0] + betas[1]*x, color="green", linewidth = 3, label = "model")
plot.xlabel('X')
plot.ylabel('Y')
_ = plot.legend(bbox_to_anchor = (1.05, 1), loc = 2, borderaxespad = 0)

model_function = lambda x: betas[0] + betas[1]*x
ok = []
too_far = []
for tx, ty in numpy.vstack((X_full, y_full)).T.tolist():
    if (model_function(tx) - ty)**2 < std_err:
        ok.append([tx, ty])
    else:
        too_far.append([tx, ty])

ok_points = numpy.array(ok)
too_far = numpy.array(too_far)
print (ok_points.shape)
print (too_far.shape)

_ = plot.plot(x, betas[0] + betas[1]*x, color="blue", linewidth = 1, label = "model")
_ = plot.plot(ok_points[:, 0], ok_points[:, 1], "g.", label = "ok points (dist. < std)")
_ = plot.plot(too_far[:, 0], too_far[:, 1], "r.", label = "points, that are too far (dist.>std)")
_ = plot.legend(bbox_to_anchor = (1.05, 1),loc = "best",borderaxespad = 0)

