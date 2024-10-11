import random
num_points=500
x_max=100
y_max=100
x_points=[]
y_points=[]
for i in range(num_points):
    x_points.append(random.random()* x_max)
    y_points.append(random.random() * y_max)
print(x_points)
print(y_points)
def f(x):
    return x * 1.2 + 50




