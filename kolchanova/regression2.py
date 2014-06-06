#!/usr/bin/python
import scipy
import numpy


xfile = open ('x.txt', 'r')
yfile = open ('y.txt','r')

xmatrix = [[float(x) for x in row.split()] for row in xfile]
	
print numpy.matrix(xmatrix).shape
x_matrix = numpy.matrix(xmatrix)


ymatrix = [[ float(y) ] for y in yfile]

print numpy.matrix(ymatrix).shape
y_matrix = numpy.matrix(ymatrix)

add_column = numpy.matrix([1]*x_matrix.shape[0]).T
new_x = numpy.hstack((add_column, x_matrix))

#matrices multiplication

step_one = numpy.dot (new_x.T, new_x)
step_two = numpy.linalg.pinv(step_one)
step_three = numpy.dot(step_two, new_x.T)


coeffs = numpy.dot(step_three, y_matrix)
errors = y_matrix - numpy.dot(new_x, coeffs)

print coeffs
#the model is too complicated (multidimentional)
#are errors distributed normally? if yes, then the model is accurate

import numpy as np
import numpy.ma as ma
from scipy.stats import mstats

x = np.array(errors) 

z,pval = mstats.normaltest(x) #Tests whether a sample differs from a normal distribution.
#This function tests the null hypothesis that a sample comes from a normal distribution
print "Z-score:", z 
print "P-value:", pval

if(pval < 0.055):
    print "Not normal distribution"
if (pval >= 0.055):
	print "This seems to be a normal distribution! Our model is good"