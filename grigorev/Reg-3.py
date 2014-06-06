#!/usr/bin/python
from __future__ import division
from sklearn.utils import shuffle
from scipy.stats import linregress
import numpy

def random_model(beta_range, set_size):
	# generate random coefficients (betas)
	min_beta, max_beta = beta_range
	model_betas = numpy.random.random_sample(2) * (max_beta - min_beta) + min_beta
	# generate points according to model betas
	X = numpy.linspace(0, 1, set_size)
	y = model_betas[0] + model_betas[1] * X
	# introduce error
	for index, _ in enumerate(y):
		y[index] += numpy.random.randn()
	#
	return (model_betas, X, y)

def split_set(X, y, train_set_fraction):
	# make data unordered
	X, y = shuffle(X, y, random_state = 1)
	# pick training set
	train = lambda: None
	train_set_size = int(y.shape[0] * train_set_fraction)
	train.X = X[:train_set_size]
	train.y = y[:train_set_size]
	# pick testing set
	test = lambda: None
	test.X = X[train_set_size:]
	test.y = y[train_set_size:]
	#
	return (train, test)

def regress(train, test):
	# perform linear regression on the training set
	betas, residuals, _, _, _ = numpy.polyfit(
		train.X,
		train.y,
		deg = 1,
		full = True
	)
	# default order of betas from polyfit doesn't really make sense
	betas = betas[::-1]
	# proposed model as function
	f = lambda x: betas[0] + betas[1] * x
	# residual sum of squares for training set is given by polyfit
	train_RSS = residuals[0]
	# calculate residual sum of squares for testing set
	test_RSS = sum([
		(f(tx) - ty)**2
		for tx, ty in
		numpy.vstack((test.X, test.y)).T.tolist()
	])
	#
	return betas, train_RSS, test_RSS

def sort_by_error_margin(X, y, std_err):
	good, bad = [], []
	f = lambda x: betas[0] + betas[1] * x
	for tx, ty in numpy.vstack((X, y)).T.tolist():
		if (f(tx) - ty)**2 < std_err:
			good.append([tx, ty])
		else:
			bad.append([tx, ty])
	return (
		numpy.array(good),
		numpy.array(bad)
	)


model_betas, X, y = random_model(beta_range = (-5, 5), set_size = 1000)
train, test = split_set(X, y, train_set_fraction = 0.8)
betas, train_RSS, test_RSS = regress(train, test)
_, _, r_value, p_value, std_err = linregress(X, y)
good, bad = sort_by_error_margin(X, y, std_err)

print("Original model: y = {0} + {1}*x".format(model_betas[0], model_betas[1]))
print("Regression: y = {0} + {1}*x".format(betas[0], betas[1]))
print("RSS/n for training set: {0}".format(train_RSS / train.y.shape[0]))
print("RSS/n for testing set:  {0}".format(test_RSS / test.y.shape[0]))
print("R^2 = {0}\np-value = {1}".format(r_value**2, p_value))
print("Size of good set: {0}".format(good.shape[0]))
print("Size of bad set: {0}".format(bad.shape[0]))
