import random

class Perceptron:
    def __init__(self, no, learning_rate=0.00001):
        # Set initial values
        self.learnc = learning_rate
        self.bias = 1

        # Compute random weights
        self.weights = []
        for i in range(no + 1):
            self.weights.append(random.uniform(-1, 1))  # Generates a random float between -1 and 1
