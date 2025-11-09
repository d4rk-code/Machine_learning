''' trying to implement k means clustering from scratch '''

import pandas as pd 
import matplotlib.pyplot as plt

#reading data

data = pd.read_csv("kmeans_dataset.csv")
x = data["X"].to_list()
y = data["Y"].to_list()

#implementing the algorithm

# step 1 : select the k centroids , step 2: categorize the given points according to the k centroids
# step 3 : recalculate the position of the centroids

k = 3

# random selection of centroids
c = [[2.08,8.01],[7.05,7.02],[1.88,1.88]]
point = [2.67,6.52]


def euclidian_distance(x , x_):
    dist_x = (x[0] - x_[0])**2 
    dist_y = (x[1] - x_[1])**2 
    d = (dist_x + dist_y)**0.5
    return d

dist = euclidian_distance(c[0], point)
print(dist)

#plot of the data
#plt.scatter(x,y)
#plt.show()
