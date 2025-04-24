import numpy as np
import random
def fitness_function(x):
    return x ** 2
def tournament_selection(population, fitness_values, num_parents, tournament_size=3):
    selected_parents = []
    for _ in range(num_parents):
        tournament_indices = np.random.choice(len(population), tournament_size, replace=False)
        tournament_population = population[tournament_indices]
        tournament_fitness = fitness_values[tournament_indices]
        winner_index = np.argmax(tournament_fitness)
        selected_parents.append(tournament_population[winner_index])
    return selected_parents
if __name__ == "__main__":
    population = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    fitness_values = np.array([fitness_function(x) for x in population])
    num_parents = 5
    tournament_size = 3
    selected_parents = tournament_selection(population, fitness_values, num_parents, tournament_size)
    print(f"Selected Parents: {selected_parents}")
