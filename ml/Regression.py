
# coding: utf-8

## Homework 3 (Linear regression)

#### Author: Anton Bragin

#### Generate data

# Generate and plot 1000 (x, y) points that are on the same line

# In[111]:

#Enable graph embedding into notebook pages
get_ipython().magic(u'matplotlib inline')


# In[112]:

import numpy
import scipy
from matplotlib import pyplot

orig_model = [7, 25]

x = numpy.linspace(0, 100, 1000)
y = orig_model[0] * x + orig_model[1]

pyplot.plot(x, y, '.')
pyplot.title('Randomly generated points')
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.show()


# Create noise with normal distribution

# In[113]:

noise = numpy.random.normal(0, 75, len(y))
pyplot.hist(noise, bins=100)
pyplot.title('Random noise with normal distribution')
pyplot.show()


# Add noise to y-coordinates and plot (x, y) points

# In[114]:

y_noise = y + noise
pyplot.plot(x, y_noise, '.')
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.title('Original data with noise added to y values')
pyplot.show()


# Splitting data into two cohorts: for education and testing

# In[115]:

#Do random sampling
samples = [_ for _ in range(len(y))]
numpy.random.shuffle(samples)

edu_size = 0.7 * len(y)
test_size = 1000 - edu_size

x_edu = []
y_edu = []
x_test = []
y_test = []

for i in range(len(samples)):
    if i < edu_size:
        x_edu.append(x[samples[i]])
        y_edu.append(y_noise[samples[i]])
    else:
        x_test.append(x[samples[i]])
        y_test.append(y_noise[samples[i]])
#Plot data for education and data for testing
pyplot.plot(x_edu, y_edu, '.b')
pyplot.plot(x_test, y_test, '.r')
pyplot.title('Educational and test data')
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.show()


#### Do linear regression for the education cohort

# In[116]:

model = numpy.polyfit(x_edu, y_edu, 1)
print('Parameters for linear model are: b1 = {}, b0 = {}'.format(model[0], model[1]))


# Plot education cohort and linear fit

# In[117]:

pyplot.plot(x_edu, y_edu, '.b')
pyplot.plot(x_edu, numpy.polyval(model, x_edu), '-r')
pyplot.title('Linear fit of educational data')
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.show()


#### Calculate RSS (residual sum of squares) for educational and testing cohorts

# In[118]:

from scipy.stats import pearsonr

def rss(x, y, model):
    y_model = numpy.polyval(model, x)
    rss = 0
    for y_d, y_m in zip(y, y_model):
        rss += (y_d - y_m) ** 2
    return rss

def r_square(x, y, model):
    ss_res = rss(x, y, model)
    ss_tot = 0
    y_mean = numpy.mean(y)
    for y_d in y:
        ss_tot += (y_d - y_mean) ** 2
    return 1 - ss_res/ss_tot
    
print('RSS for education data: {}'.format(rss(x_edu, y_edu, model)))
print('RSS for testing data: {}'.format(rss(x_test, y_test, model)))
print('R2 for the whole dataset is: {}'.format(r_square(x, y_noise, model)))
print('Pearson correlation coeficient is: {}'.format(*pearsonr(x, y_noise)))


#### Check linearity hypotesis

# The null hypothesis states that the slope is equal to zero, and the alternative hypothesis states that the slope is not equal to zero.
# Set statistical significance level to 0.01 and calculate sum of squares and p-value. The hypotesis is that noise has normal distribution.

# In[119]:

stat_significance = 0.99
slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x,y_noise)
print('R-value is: {}'.format(r_value))
print('t-statistic is: {}'.format(std_err / model[0]))
print('P-value is: {0:0.2e}'.format(p_value))


#### Plot graphs from the task

# In[120]:

pyplot.plot(x_edu, y_edu, '.b')
pyplot.plot(x_test, y_test, '.r')
pyplot.plot(x_edu, numpy.polyval(model, x_edu), '-k')
pyplot.plot(x, numpy.polyval(orig_model, x), '-c')
#Add legend
pyplot.xlabel('x')
pyplot.ylabel('y')
e_legend = pyplot.Rectangle((0, 0), 1, 1, fc="b")
t_legend = pyplot.Rectangle((0, 0), 1, 1, fc="r")
r_legend = pyplot.Rectangle((0, 0), 1, 1, fc="k")
i_legend = pyplot.Rectangle((0, 0), 1, 1, fc="c")
pyplot.legend([e_legend, t_legend, r_legend, i_legend], 
              ['Education cohort', 'Test cohort', 'Regression model', 'Original model'], loc=4)
pyplot.show()


# In[121]:

#Calculate mean sum of squares for the whole dataset
mss = pow(rss(x, y_noise, model) / len(x), 0.5)

y_model = numpy.polyval(model, x)

x_in_mss = []
y_in_mss = []
x_out_mss = []
y_out_mss = []

for i in range(len(x)):
    if abs(y_model[i] - y_noise[i]) <= mss:
        x_in_mss.append(x[i])
        y_in_mss.append(y_noise[i])
    else:
        x_out_mss.append(x[i])
        y_out_mss.append(y_noise[i])

pyplot.plot(x_in_mss, y_in_mss, '.b')
pyplot.plot(x_out_mss, y_out_mss, '.r')
pyplot.plot(x_edu, numpy.polyval(model, x_edu), '-k')
#Add legend
pyplot.xlabel('x')
pyplot.ylabel('y')
in_legend = pyplot.Rectangle((0, 0), 1, 1, fc="b")
out_legend = pyplot.Rectangle((0, 0), 1, 1, fc="r")
pyplot.legend([in_legend, out_legend], 
              ['Points within MSS', 'Points outside of MSS'], loc=4)
pyplot.show()

