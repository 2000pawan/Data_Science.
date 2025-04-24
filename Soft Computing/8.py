import numpy as np
import matplotlib.pyplot as plt

class AdaptiveFilterANN:
 def __init__(self, input_size, hidden_size, output_size):
  self.weights_input_hidden = np.random.randn(input_size, hidden_size) * 0.1
  self.bias_hidden = np.zeros((1, hidden_size))
  self.weights_hidden_output = np.random.randn(hidden_size, output_size) * 0.1
  self.bias_output = np.zeros((1, output_size))

 def sigmoid(self, x):
  return 1 / (1 + np.exp(-x))

 def sigmoid_derivative(self, x):
  return x * (1 - x)

 def forward(self, X):
  self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
  self.hidden_output = self.sigmoid(self.hidden_input)
  self.output_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
  self.output = self.sigmoid(self.output_input)
  return self.output

 def backward(self, X, y, learning_rate=0.01):
  output_error = y - self.output
  output_delta = output_error * self.sigmoid_derivative(self.output)
  hidden_error = output_delta.dot(self.weights_hidden_output.T)
  hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden_output)
  self.weights_hidden_output += self.hidden_output.T.dot(output_delta) * learning_rate
  self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
  self.weights_input_hidden += X.T.dot(hidden_delta) * learning_rate
  self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

 def train(self, X, y, epochs=1000, learning_rate=0.01):
  for epoch in range(epochs):
   self.forward(X)
   self.backward(X, y, learning_rate)
   if epoch % 100 == 0:
    loss = np.mean(np.square(y - self.output))
    print(f"Epoch {epoch}/{epochs}, Loss: {loss:.5f}")

 def predict(self, X):
  return self.forward(X)

def generate_signal(t, frequency=1.0):
 return np.sin(2 * np.pi * frequency * t)

def add_noise_to_signal(signal, noise_level=0.5):
 noise = np.random.normal(0, noise_level, signal.shape)
 return signal + noise

t = np.linspace(0, 10, 1000)
clean_signal = generate_signal(t)
noisy_signal = add_noise_to_signal(clean_signal)
X = noisy_signal.reshape(-1, 1)
y = clean_signal.reshape(-1, 1)

input_size = 1
hidden_size = 10
output_size = 1
ann = AdaptiveFilterANN(input_size, hidden_size, output_size)
ann.train(X, y, epochs=1000, learning_rate=0.01)
filtered_signal = ann.predict(X)

plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(t, clean_signal, color="blue")
plt.title("Clean Signal (Desired Output)")
plt.subplot(3, 1, 2)
plt.plot(t, noisy_signal, color="red")
plt.title("Noisy Signal (Input to Adaptive Filter)")
plt.subplot(3, 1, 3)
plt.plot(t, filtered_signal, color="green")
plt.title("Filtered Signal (Output of Adaptive Filter)")
plt.tight_layout()
plt.show()
