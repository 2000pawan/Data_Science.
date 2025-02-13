import numpy as np

class DiscretePerceptron:
    def __init__(self, input_size):
        self.weights = np.zeros(input_size)
        self.bias = 0

    def predict(self, inputs):
        activation = np.dot(self.weights, inputs) + self.bias
        return 1 if activation > 0 else 0

    def train(self, inputs, target, learning_rate=0.1, epochs=100):
        for _ in range(epochs):
            for x, y in zip(inputs, target):
                prediction = self.predict(x)
                error = y - prediction
                self.weights += learning_rate * error * x
                self.bias += learning_rate * error

def main():
    # Generate some example data points for two classes
    class_0 = np.array([[2, 3], [3, 2], [1, 1]])
    class_1 = np.array([[5, 7], [6, 8], [7, 6]])
    
    # Combine the data points and create labels (0 for class 0, 1 for class 1)
    inputs = np.vstack((class_0, class_1))
    targets = np.array([0, 0, 0, 1, 1, 1])
    
    # Create a discrete perceptron with input size 2
    perceptron = DiscretePerceptron(input_size=2)

    # Train the perceptron
    perceptron.train(inputs, targets)

    # Test the trained perceptron with new data
    test_data = np.array([[4, 5], [2, 2]])
    for data in test_data:
        prediction = perceptron.predict(data)
        if prediction == 0:
            print(f"Data {data} belongs to class 0")
        else:
            print(f"Data {data} belongs to class 1")

if __name__ == "__main__":
    main()
