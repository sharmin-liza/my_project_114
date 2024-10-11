import random
import numpy as np
import matplotlib.pyplot as plt

# Perceptron class ---------------------
class Perceptron:
    def __init__(self, no, learning_rate=0.00001):
        # Set initial values
        self.learnc = learning_rate
        self.bias = 1

        # Compute random weights
        self.weights = [random.uniform(-1, 1) for _ in range(no + 1)]

    # Activate Function
    def activate(self, inputs):
        sum_val = 0
        for i in range(len(inputs)):
            sum_val += inputs[i] * self.weights[i]
        return 1 if sum_val > 0 else 0

    # Train Function
    def train(self, inputs, desired):
        inputs.append(self.bias)  # Add bias to inputs
        guess = self.activate(inputs)
        error = desired - guess
        if error != 0:
            for i in range(len(inputs)):
                self.weights[i] += self.learnc * error * inputs[i]


# Initialize values
num_points = 500
learning_rate = 0.00001

# Create Random XY Points
x_max, y_max = 400, 400
x_points = [random.random() * x_max for _ in range(num_points)]
y_points = [random.random() * y_max for _ in range(num_points)]

# Line function
def f(x):
    return x * 1.2 + 50

# Compute desired answers
desired = []
for i in range(num_points):
    if y_points[i] > f(x_points[i]):
        desired.append(1)
    else:
        desired.append(0)

# Create a Perceptron
ptron = Perceptron(2, learning_rate)

# Train the Perceptron
for _ in range(10000):
    for i in range(num_points):
        ptron.train([x_points[i], y_points[i]], desired[i])

# Plot the results
fig, ax = plt.subplots()
ax.set_xlim([0, x_max])
ax.set_ylim([0, y_max])

# Plot the line
x_vals = np.linspace(0, x_max, 100)
y_vals = f(x_vals)
ax.plot(x_vals, y_vals, 'k')  # 'k' for black color

# Plot the points
for i in range(num_points):
    x, y = x_points[i], y_points[i]
    guess = ptron.activate([x, y, ptron.bias])
    color = 'blue' if guess == 0 else 'black'
    ax.plot(x, y, 'o', color=color)

plt.show()
