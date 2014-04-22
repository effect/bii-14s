#!/usr/bin/python

#I chose to perform the classification task using the KNN method
import sys
import numpy as np
import scipy
from sklearn.utils import shuffle
import matplotlib.pyplot as plot
from sklearn.neighbors import KNeighborsClassifier

blue = np.loadtxt("./blue.txt")
red = np.loadtxt("./red.txt")

#Visualize data (this doesn't work outside ipython), but we get something
#like an ellipse.... (pic attached) 

#_ = plot.plot(blue[:, 0], blue[:, 1], "b.")
#_ = plot.plot(red[:, 0],  red[:, 1],  "r.")


#Create the classifying function

red_points = np.hstack ((red, [[1]] * len (red) ))
blue_points = np.hstack  ((blue, [[0]] * len (blue) ))
all_points = np.concatenate((red_points, blue_points), axis=0)

x = all_points[:, :-1]
y = all_points[:, 2]
x, y = shuffle(x, y, random_state=1)


train_set=all_points.shape[0] *0.6
Xtrainset = x[:train_set]
Ytrainset = y[:train_set]
Xtestset = x[train_set:]
Ytestset = y[train_set:]

knearest = KNeighborsClassifier(n_neighbors=5)
knearest.fit(Xtrainset, Ytrainset)
print 'Training set score:', knearest.score(Xtrainset, Ytrainset)
print 'Test set score:', knearest.score(Xtestset, Ytestset)

#Prediction function

def classify (x,y):
	if knearest.predict([x,y]) == 0:
		print "must be blue..."
	else:
		print "must be red..."

#propose some coordinates :)
print 'what will be your x?'
x = raw_input()
print 'and y?'
y = raw_input()

classify (x,y) 
