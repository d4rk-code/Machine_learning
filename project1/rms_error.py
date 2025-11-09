import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('file.csv')

time = data["Time_Spent_With_Family_Hours"].to_list()
scores = data["Happiness_Score"].to_list()


# updated linear regression ------

def Gradient(m_ , b_ , L , points):
    
    grad_m = 0
    grad_b = 0

    n = len(points)

    for i in range(n):

        x = time[i]
        y = scores[i]

        #partial derivative of root of mean squared error

        grad_m += -(1/(n**0.5)) * x
        grad_b += -(1/(n**0.5)) 

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

