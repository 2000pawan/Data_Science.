import numpy as np
import random

# A simple fitness function (for example, maximize f(x) = x^2)
def fitness_function(x):
    return x ** 2  # Fitness of x is x squared

# Roulette Wheel Selection
def roulette_wheel_selection(population, fitness_values):
    # Step 1: Calculate the total fitness
    total_fitness = sum(fitness_values)

    # Step 2: Calculate selection probabilities for each individual
    selection_probs = [fitness / total_fitness for fitness in fitness_values]

    # Step 3: Create the cumulative distribution
    cumulative_probs = np.cumsum(selection_probs)

    # Step 4: Select individuals based on cumulative probabilities
    rand_value = random.random()  # Random number between 0 and 1

    # Find the individual based on the random number
    for i, cumulative_prob in enumerate(cumulative_probs):
        if rand_value < cumulative_prob:
            return population[i]

# Example to run the Roulette Wheel Selection
if __name__ == "__main__":
    # Create a population of individuals (simple range of numbers in this case)
    population = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # Calculate fitness values for each individual
    fitness_values = np.array([fitness_function(x) for x in population])

    # Number of selections we want to make
    num_selections = 5
    selected_individuals = []

    for _ in range(num_selections):
        selected = roulette_wheel_selection(population, fitness_values)
        selected_individuals.append(selected)

    print(f"Selected Individuals: {selected_individuals}")
