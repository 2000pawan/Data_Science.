import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1):
        self.weights = np.zeros(input_size)  # Initialize weights to zeros
        self.bias = 0                        # Initialize bias to zero
        self.learning_rate = learning_rate

    def step_function(self, x):
        """Activation function: step function."""
        return 1 if x >= 0 else 0

    def predict(self, X):
        """Predict the class of the input X."""
        linear_output = np.dot(X, self.weights) + self.bias
        return self.step_function(linear_output)

    def fit(self, X, y, epochs=100):
        """Train the perceptron using the Perceptron learning rule."""
        for epoch in range(epochs):
            for i in range(len(X)):
                prediction = self.predict(X[i])
                error = y[i] - prediction
                # Update weights and bias based on error
                self.weights += self.learning_rate * error * X[i]
                self.bias += self.learning_rate * error

    def plot_decision_boundary(self, X, y):
        """Plot the decision boundary."""
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                             np.arange(y_min, y_max, 0.1))
        Z = np.array([self.predict(np.array([xx_i, yy_i])) 
                      for xx_i, yy_i in zip(xx.ravel(), yy.ravel())])
        Z = Z.reshape(xx.shape)

        plt.contourf(xx, yy, Z, alpha=0.8)
        plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.coolwarm)
        plt.xlabel("X1")
        plt.ylabel("X2")
        plt.title("Perceptron Decision Boundary")
        plt.show()

# AND Logic (Linearly separable)
X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([0, 0, 0, 1])

# XOR Logic (Non-linearly separable)
X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_xor = np.array([0, 1, 1, 0])

# Train and test on AND Logic (Linearly separable)
print("Training on AND Logic (Linearly separable):")
perceptron_and = Perceptron(input_size=2)
perceptron_and.fit(X_and, y_and, epochs=10)
perceptron_and.plot_decision_boundary(X_and, y_and)

# Train and test on XOR Logic (Non-linearly separable)
print("Training on XOR Logic (Non-linearly separable):")
perceptron_xor = Perceptron(input_size=2)
perceptron_xor.fit(X_xor, y_xor, epochs=10)
perceptron_xor.plot_decision_boundary(X_xor, y_xor)
