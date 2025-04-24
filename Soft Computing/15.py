import numpy as np
import random
import matplotlib.pyplot as plt

def fitness_function(x):
    return x ** 2

def sigma_scaling(population, fitness_values):
    mu = np.mean(fitness_values)
    sigma = np.std(fitness_values)
    epsilon = 1e-6
    scaled_fitness = (fitness_values - mu) / (sigma + epsilon)
    return scaled_fitness

if __name__ == "__main__":
    population = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    fitness_values = np.array([fitness_function(x) for x in population])
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.bar(population, fitness_values, color='blue', alpha=0.7)
    plt.title('Original Fitness Values')
    plt.xlabel('Individual')
    plt.ylabel('Fitness')
    scaled_fitness_values = sigma_scaling(population, fitness_values)
    plt.subplot(1, 2, 2)
    plt.bar(population, scaled_fitness_values, color='green', alpha=0.7)
    plt.title('Scaled Fitness Values (Sigma Scaling)')
    plt.xlabel('Individual')
    plt.ylabel('Scaled Fitness')
    plt.tight_layout()
    plt.show()
    print(f"Original Fitness Values: {fitness_values}")
    print(f"Scaled Fitness Values (Sigma Scaling): {scaled_fitness_values}")
