''' trying to implement k means clustering from scratch '''

import pandas as pd 
import matplotlib.pyplot as plt
import random

'''reading data'''

data = pd.read_csv("kmeans_dataset.csv")
x = data["X"].to_list()
y = data["Y"].to_list()

'''implementing the algorithm'''

# step 1 : select the k centroids , step 2: categorize the given points according to the k centroids
# step 3 : recalculate the position of the centroids

k = 3 # because the dataset that i chose has 3 clusters provided


# random selection of centroids
#c = [[2.08,8.01],[7.05,7.02],[1.88,1.88]]  desired centroids

c = []

for j in range(3):
    c.append([random.uniform(0.00,9.50),random.uniform(0.00,9.00)])


def euclidian_distance(x , x_):
    dist = ((x[0] - x_[0])**2 + (x[1] - x_[1])**2)**0.5
    return dist

#find the minimum distances between the centroids and the points in the dataset

l = []

for i in range(len(x)):
    #print([x[i],y[i]])
    q = []
    for j in range(k):
        d = euclidian_distance([x[i],y[i]], c[j])
        q.append([d,[x[i],y[i]]])
    l.append(q)


# the nearest distance
l.sort()


m = [] # so we got the coordinates of the points with the nearest distances


for i in range(k):
    m.append(l[i][1][1])

print(m)



# classification 
# -> the task is to find the coordinate of the data point from which there is the least distance of the centroid




# recalculation of the centroids




'''plot of the data'''


#plt.scatter(x,y)
#plt.scatter(c[0][:], c[1][:])
#plt.show()
