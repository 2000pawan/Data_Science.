import numpy as np
import matplotlib.pyplot as plt

def rastrigin_function(x, A=10):
    return A * len(x) + np.sum(x**2 - A * np.cos(2 * np.pi * x))

def initialize_population(pop_size, dimension, lower_bound, upper_bound):
    return np.random.uniform(lower_bound, upper_bound, (pop_size, dimension))

def evaluate_fitness(population):
    return np.apply_along_axis(rastrigin_function, 1, population)

def select_parents(population, fitness, num_parents):
    fitness = 1 / (1 + fitness)
    selection_prob = fitness / np.sum(fitness)
    parents_idx = np.random.choice(range(len(population)), size=num_parents, p=selection_prob)
    return population[parents_idx]

def crossover(parents, crossover_rate):
    num_parents = len(parents)
    offspring = np.copy(parents)
    for i in range(0, num_parents, 2):
        if np.random.rand() < crossover_rate:
            crossover_point = np.random.randint(1, parents.shape[1])
            offspring[i, crossover_point:], offspring[i+1, crossover_point:] = offspring[i+1, crossover_point:].copy(), offspring[i, crossover_point:].copy()
    return offspring

def mutate(offspring, mutation_rate, lower_bound, upper_bound):
    mutation = np.random.rand(*offspring.shape) < mutation_rate
    random_mutation = np.random.uniform(lower_bound, upper_bound, offspring.shape)
    offspring[mutation] = random_mutation[mutation]
    return offspring

def genetic_algorithm(pop_size, dimension, lower_bound, upper_bound, num_generations, crossover_rate, mutation_rate):
    population = initialize_population(pop_size, dimension, lower_bound, upper_bound)
    best_solution = None
    best_fitness = float('inf')
    global best_fitness_history
    best_fitness_history = []
    for generation in range(num_generations):
        fitness = evaluate_fitness(population)
        generation_best_fitness = np.min(fitness)
        generation_best_solution = population[np.argmin(fitness)]
        best_fitness_history.append(generation_best_fitness)
        if generation_best_fitness < best_fitness:
            best_fitness = generation_best_fitness
            best_solution = generation_best_solution
        num_parents = pop_size // 2
        parents = select_parents(population, fitness, num_parents)
        offspring = crossover(parents, crossover_rate)
        offspring = mutate(offspring, mutation_rate, lower_bound, upper_bound)
        population[:num_parents] = parents
        population[num_parents:] = offspring
        if generation % 100 == 0:
            print(f"Generation {generation}: Best Fitness = {best_fitness:.5f}")
    return best_solution, best_fitness

pop_size = 100
dimension = 10
lower_bound = -5.12
upper_bound = 5.12
num_generations = 1000
crossover_rate = 0.7
mutation_rate = 0.02

best_solution, best_fitness = genetic_algorithm(pop_size, dimension, lower_bound, upper_bound, num_generations, crossover_rate, mutation_rate)
print(f"Best solution found: {best_solution}")
print(f"Best fitness: {best_fitness}")

plt.plot(range(num_generations), best_fitness_history)
plt.title("Best Fitness Over Generations")
plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.show()
