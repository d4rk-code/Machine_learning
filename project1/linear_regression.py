''' 

First linear regression model training from scratch no library

time spent with family v/s happiness score 

''' 


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('training_set.csv')

time = data["Time_Spent_With_Family_Hours"].to_list()
scores = data["Happiness_Score"].to_list()


# linear regression ------

def Gradient(m_ , b_ , L , points):
    
    grad_m = 0
    grad_b = 0

    n = len(points)

    for i in range(n):

        x = time[i]
        y = scores[i]

        grad_m += -(2/n) * x * ( y - (m_ * x + b_))
        grad_b += -(2/n) * ( y - (m_ * x + b_))

    m = m_ - L*grad_m
    b = b_ - L*grad_b
    
    return m , b


m = 0
b = 0
L = 0.0001
epochs = int(input("enter number of epochs: "))

for i in range(epochs):
    m , b = Gradient(m , b , L , data)

print(f"{epochs} epochs completed")

y = []

for x in time:
    y.append(m*x+b)

plt.scatter(data.Time_Spent_With_Family_Hours, data.Happiness_Score)
plt.plot(time, y)
plt.show()



