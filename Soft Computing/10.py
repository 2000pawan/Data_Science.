import numpy as np
import matplotlib.pyplot as plt
import random

# Euclidean distance function
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate the total distance of a given route
def calculate_total_distance(route, cities):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += euclidean_distance(cities[route[i]], cities[route[i + 1]])
    total_distance += euclidean_distance(cities[route[-1]], cities[route[0]])  # Return to start
    return total_distance

# Initialize the population
def initialize_population(pop_size, num_cities):
    return [np.random.permutation(num_cities) for _ in range(pop_size)]

# Tournament selection
def tournament_selection(population, fitness, tournament_size=3):
    selected_parents = []
    for _ in range(2):  # Select two parents
        tournament = random.sample(range(len(population)), tournament_size)
        tournament_fitness = [fitness[i] for i in tournament]
        winner_idx = tournament[np.argmin(tournament_fitness)]
        selected_parents.append(population[winner_idx])
    return selected_parents

# PMX Crossover
def pmx_crossover(parent1, parent2):
    size = len(parent1)
    crossover_point1 = random.randint(0, size // 2)
    crossover_point2 = random.randint(size // 2, size)

    def pmx_offspring(p1, p2):
        offspring = [-1] * size
        offspring[crossover_point1:crossover_point2] = p1[crossover_point1:crossover_point2]
        for i in range(crossover_point1, crossover_point2):
            if p2[i] not in offspring:
                pos = i
                while crossover_point1 <= pos < crossover_point2:
                    pos = np.where(p2 == p1[pos])[0][0]
                offspring[pos] = p2[i]
        for i in range(size):
            if offspring[i] == -1:
                offspring[i] = p2[i]
        return np.array(offspring)

    return pmx_offspring(parent2, parent1), pmx_offspring(parent1, parent2)

# Swap Mutation
def swap_mutation(route):
    idx1, idx2 = random.sample(range(len(route)), 2)
    route[idx1], route[idx2] = route[idx2], route[idx1]
    return route

# Main Genetic Algorithm
def genetic_algorithm(cities, pop_size=100, num_generations=1000, mutation_rate=0.1, tournament_size=3):
    num_cities = len(cities)
    population = initialize_population(pop_size, num_cities)
    best_route = None
    best_distance = float('inf')

    for generation in range(num_generations):
        fitness = [calculate_total_distance(route, cities) for route in population]
        min_fitness = min(fitness)

        if min_fitness < best_distance:
            best_distance = min_fitness
            best_route = population[np.argmin(fitness)]

        new_population = []
        while len(new_population) < pop_size:
            parents = tournament_selection(population, fitness, tournament_size)
            offspring1, offspring2 = pmx_crossover(parents[0], parents[1])
            if random.random() < mutation_rate:
                offspring1 = swap_mutation(offspring1)
            if random.random() < mutation_rate:
                offspring2 = swap_mutation(offspring2)
            new_population.append(offspring1)
            if len(new_population) < pop_size:
                new_population.append(offspring2)

        population = new_population[:pop_size]

        if generation % 100 == 0:
            print(f"Generation {generation}: Best Distance = {best_distance:.2f}")

    return best_route, best_distance

# Generate random cities
def generate_cities(num_cities=20):
    return np.random.rand(num_cities, 2) * 100

# Visualize the route
def plot_route(route, cities):
    route_cities = cities[route]
    plt.plot(route_cities[:, 0], route_cities[:, 1], 'bo-')
    plt.plot(route_cities[0, 0], route_cities[0, 1], 'ro')  # Start city
    plt.title("Best Route Found")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

# Run the program
if __name__ == "__main__":
    num_cities = 20
    cities = generate_cities(num_cities)
    best_route, best_distance = genetic_algorithm(cities, pop_size=100, num_generations=1000, mutation_rate=0.05)
    print(f"Best Distance: {best_distance:.2f}")
    plot_route(best_route, cities)
