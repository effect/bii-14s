import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from matplotlib.colors import ListedColormap
red_dots = np.loadtxt("red.txt")
blue_dots = np.loadtxt("blue.txt")
#plt.plot(red_dots[:, 0], red_dots[:, 1], '.', color='red')
#plt.plot(blue_dots[:, 0], blue_dots[:, 1], '.', color='blue')
#plt.show()

red_class = np.array(([1])*len(red_dots))  # red is 1
red_class = red_class.reshape(red_class.size, 1)
blue_class = np.array(([0])*len(blue_dots))  # blue is 0
blue_class = blue_class.reshape(blue_class.size, 1)
total_class = np.concatenate((red_class, blue_class))
total_dots = np.concatenate((red_dots, blue_dots))

shuffled_total_dots, shuffled_total_class = shuffle(total_dots, total_class)
shuffled_total_class = shuffled_total_class.reshape(total_class.size, )
dots_train = shuffled_total_dots[:950]
class_train = shuffled_total_class[:950]
dots_test = shuffled_total_dots[950:]
class_test = shuffled_total_class[950:]

knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(dots_train, class_train)
print 'Accuracy of KNN train set:', knn.score(dots_train, class_train)
print 'Accuracy of KNN test set:', knn.score(dots_test, class_test)
def plot_knn(X):
    h = .018
    cmap_light = ListedColormap(['#0000FF', '#FF0000'])
    x_min, x_max = X[:, 0].min(), X[:, 0].max()
    y_min, y_max = X[:, 1].min(), X[:, 1].max()
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.scatter(shuffled_total_dots[:, 0], shuffled_total_dots[:, 1], c=shuffled_total_class, cmap=cmap_light)
    plt.scatter(xx, yy, Z)
    plt.title('k Nearest Neighbors')
    plt.show()

rfc = RandomForestClassifier(n_estimators=10)
rfc.fit(dots_train, class_train)
print 'Accuracy of Random Forest train set:', rfc.score(dots_train, class_train)
print 'Accuracy of Random Forest test set:', rfc.score(dots_test, class_test)

def plot_rfc(X):
    h = .018
    cmap_light = ListedColormap(['#0000FF', '#FF0000'])
    x_min, x_max = X[:, 0].min(), X[:, 0].max()
    y_min, y_max = X[:, 1].min(), X[:, 1].max()
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = rfc.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.scatter(shuffled_total_dots[:, 0], shuffled_total_dots[:, 1], c = shuffled_total_class, cmap=cmap_light)
    plt.scatter(xx, yy, Z)
    plt.title('Random Forest')
    plt.show()

def what_is_the_color_of_the_dot_knn(coord_x, coord_y):
    list = [coord_x, coord_y]
    if knn.predict(list) == 1:
        return 'KNN decision: Red'
    else:
        return 'KNN decision: Blue'

def what_is_the_color_of_the_dot_rfc(coord_x, coord_y):
    list = [coord_x, coord_y]
    if rfc.predict(list) == 1:
        return 'RF decision: Red'
    else:
        return 'RF decision: Blue'


print what_is_the_color_of_the_dot_knn(0.6, 0.47)
print what_is_the_color_of_the_dot_rfc(0.6, 0.47)

plot_knn(dots_test)
plot_rfc(dots_test)
