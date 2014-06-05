import numpy as np
import matplotlib.pyplot as pl
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

#Import dataset
red = np.loadtxt("./red.txt")
blue = np.loadtxt("./blue.txt")

#Plot data
pl.prism()
plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)
pl.scatter(red[:, 0], red[:, 1], c='red')
pl.scatter(blue[:, 0], blue[:, 1], c='blue')

#Prepare data for analysis
reds = np.hstack ((red, [[1]] * len (red) ))
blues = np.hstack  ((blue, [[0]] * len (blue) ))
dots = np.concatenate((reds, blues), axis=0)
x = dots[:, :-1]
y = dots[:, 2]

#Train and test sets
x, y = shuffle(x, y, random_state=1)
size=dots.shape[0] * 0.8
x_train = x[:size]
y_train = y[:size]
x_test = x[size:]
y_test = y[size:]

#Build clussifier (KNN)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
print 'Accuracy of KNN train set:', knn.score(x_train, y_train)
print 'Accuracy of KNN test set:', knn.score(x_test, y_test)

#Plot KNN
y_pred_test_KNN = knn.predict(x_test)
plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)
plt.scatter(x_test[:, 0], x_test[:, 1], c=y_pred_test_KNN, marker='^')
plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train)

#Build clussifier (Random forest)
rf = RandomForestClassifier(n_estimators=10)
rf.fit(x_train, y_train)
print 'Accuracy of Random Forest train set:', rf.score(x_train, y_train)
print 'Accuracy of Random Forest test set:', rf.score(x_test, y_test)

#Plot RF
y_pred_test_RF = rf.predict(x_test)
plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)
plt.scatter(x_test[:, 0], x_test[:, 1], c=y_pred_test+RF, marker='^')
plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train)

#Predict color
def predict_KNN(a,b):
    if knn.predict([a, b]) == 0:
        return 'blue'
    else:
        return 'red'

def predict_RF(a,b):
    if rf.predict([a, b]) == 0:
        return 'blue'
    else:
        return 'red'

a = raw_input()
b = raw_input()
print 'Predict color KNN:', predict_KNN(a,b)
print 'Predict color RF:', predict_RF(a,b)

print 'Best model is:'
if rf.score(x_test, y_test) >= knn.score(x_test, y_test):
    print 'Random forest'
else:
    print 'K-Nearest Neighbors'