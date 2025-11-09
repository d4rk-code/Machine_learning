''' 
trying to implement k nearest neighbours algorithm from scratch
goal is to predict the car brand using the k nearest neighbours algorithm
'''

import pandas as pd
import matplotlib.pyplot as plt

''' reading the data from csv using pandas'''

data = pd.read_csv("car_knn_dataset.csv")
x = data["price_kUSD"].to_list()
y = data["common"].to_list()

x_ = float(input(f"enter price $ range({min(x)},{max(x)}): "))
y_ = float(input(f"enter the common rate(range = {min(y)},{max(y)}): "))

n = [x_,y_]  # the point to find and predict the brand name 

'''creating the functions and algorithms '''

l = []

# using the distance formula to calculate and predict the nearest distance the nearest neighbours are 4

def knn(a,k=4):
    q = []
    for i in range(len(x)):
        n_dist = ((x[i]-a[0])**2 +(y[i]-a[1])**2)**0.5
        q.append((n_dist,data["brand"][i]))
        l.append((n_dist,x[i],y[i]))
    q.sort()
    dw = q[:k]
    brands = [] 
    dic = {}
    for i in dw:
        brands.append(i[1])
    for i in brands:
        dic[i] = dic.get(i,0) + 1 

    print(max(dic,key=dic.get))

knn(n)

l.sort()
lss = l[:4]
points =  []
for i in lss:
    points.append((i[1],i[2]))
    

''' implementation and plot of the data '''
color = ["green" if val < 5.9 else "blue" for val in y]
plt.scatter(x,y,c = color)
plt.scatter(n[0],n[1],c="red")
plt.text(n[0],n[1],"Your Car",fontweight="bold")
for i,j in points:
    plt.plot([n[0],i],[n[1],j],'r--')
plt.show()
