import numpy as np
import random
def fitness_function(x):
    return x ** 2
def rank_selection(population, fitness_values, num_parents):
    sorted_indices = np.argsort(fitness_values)[::-1]
    sorted_population = population[sorted_indices]
    ranks = np.arange(1, len(population) + 1)
    total_rank = np.sum(ranks)
    selection_probs = ranks / total_rank
    selected_parents = np.random.choice(sorted_population, size=num_parents, p=selection_probs)
    return selected_parents
if __name__ == "__main__":
    population = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    fitness_values = np.array([fitness_function(x) for x in population])
    num_parents = 5
    selected_parents = rank_selection(population, fitness_values, num_parents)
    print(f"Selected Parents: {selected_parents}")
