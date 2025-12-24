import subprocess
import sys

try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
    import numpy as np

# Sigmoid Activation Function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of Sigmoid for Backpropagation
def sigmoid_derivative(x):
    return x * (1 - x)

# Training Data (Logic OR gate)
# Input: [A, B] | Output: [A OR B]
inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
targets = np.array([[0], [1], [1], [1]])

# Initialize weights randomly
np.random.seed(1)
weights = np.random.random((2, 1))

# Training Loop (10,000 iterations)
for i in range(10000):
    # 1. Forward Pass
    outputs = sigmoid(np.dot(inputs, weights))
    
    # 2. Calculate Error
    error = targets - outputs
    
    # 3. Backpropagation (Adjust Weights)
    adjustments = error * sigmoid_derivative(outputs)
    weights += np.dot(inputs.T, adjustments)

print("\n--- NEURAL NETWORK RESULTS ---")
print("Final Weights after training:")
print(weights)
print("\nPredictions (should be close to 0, 1, 1, 1):")
print(outputs)

input("\nPress Enter to close...")
