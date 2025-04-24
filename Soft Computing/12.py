import numpy as np
import random
def fitness_function(x):
    return x ** 2
def stochastic_universal_sampling(population, fitness_values, num_parents):
    total_fitness = sum(fitness_values)
    spacing = total_fitness / num_parents
    start_point = random.uniform(0, spacing)
    cumulative_fitness = np.cumsum(fitness_values)
    parents = []
    pointer = start_point
    i = 0
    for _ in range(num_parents):
        while pointer > cumulative_fitness[i]:
            i += 1
        parents.append(population[i])
        pointer += spacing
    return parents
if __name__ == "__main__":
    population = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    fitness_values = np.array([fitness_function(x) for x in population])
    num_parents = 5
    selected_parents = stochastic_universal_sampling(population, fitness_values, num_parents)
    print(f"Selected Parents: {selected_parents}")
