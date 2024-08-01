# Define the threshold, inputs, and weights
threshold = 1.5
inputs = [1, 0, 1, 0, 1]
weights = [0.7, 0.6, 0.5, 0.3, 0.4]

# Calculate the weighted sum
sum = 0
for i in range(len(inputs)):
    sum += inputs[i] * weights[i]

# Determine activation based on the threshold
activate = sum > threshold

# Print the result
print("Sum:", sum)
print("Activate:", activate)
