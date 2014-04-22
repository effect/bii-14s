#!/usr/bin/python
import numpy


yz = [1, 3, 2]
xz = [1, 2, 3]


xmatrix = [float(x) for x in xz]
print numpy.matrix(xmatrix).shape
x_matrix = numpy.matrix(xmatrix)

ymatrix = [ float(y)  for y in yz]
print numpy.matrix(ymatrix).shape
y_matrix = numpy.matrix(ymatrix)

from scipy import stats
import numpy as np
#linregress - This computes a least-squares regression for two sets of measurements.
slope, intercept, r_value, p_value, std_err = stats.linregress(xmatrix,ymatrix)
print "slope:", slope 
print "intercept:", intercept

print "standard error:", std_err
print "Coefficient of determination (R-squared):", r_value**2
print "p-value:", p_value

from scipy import polyfit
coefficients = polyfit(xz, yz, 1)[::-1]
print "coefficients (same as slope, intercept):", coefficients


#let us use the CHI-SQUARED TEST

def Sum (y_matrix, yz, xz, coefficients):
	for i in range (y_matrix.shape[0]):
		a = (sum([yz[i] - coefficients[1]*xz[i] - coefficients[0]])**2)*6

	return a
a = Sum(y_matrix, yz, xz, coefficients)


#count p-value


from scipy import stats
p_value = stats.chi2.cdf(a,3)
print "chi-squared, P-value:", p_value



