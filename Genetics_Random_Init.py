#PAPOUTSAKIS ANDREAS  Multi-Constrained Knapsack Problem  Project 
import numpy as np
import random
import time




# ---- To avoid potential errors, also load data here, do not change this ---->
root_folder = 'Public/'
W1 = np.load("weights1.npy")
W2 = np.load("weights2.npy")
W3 = np.load("weights3.npy")
V = np.load("values.npy")
capacity1, capacity2, capacity3 = 500, 750, 1000 # the boundary constraints for each W

# W1, W2, W3, V look like: [0.15795, 0.0086 , 0.7682 , ..., 0.73664, 0.50227, 0.3245]
#                       IDS:  0        1        2      ...   9997     9998     9999  # 10000 items

# <---------------------------------




# ------- Build your algorithm approach here  ---------->

np.random.seed(42)
random.seed(42)

vector_size = len(V)
population_size = 100
num_iterations = 50
mutation_rate = 0.05



def initialize_population(pop_size, genome_length, W1, W2, W3, V, max_W1=500, max_W2=750, max_W3=1000):
    population = []

    for _ in range(pop_size):
        individual = np.zeros(genome_length)
        current_W1, current_W2, current_W3 = 0, 0, 0

        indices = list(range(genome_length))
        np.random.shuffle(indices)  # Shuffle indices to select items randomly

        for idx in indices:
            if (current_W1 + W1[idx] <= max_W1 and
                current_W2 + W2[idx] <= max_W2 and
                current_W3 + W3[idx] <= max_W3):
                individual[idx] = 1
                current_W1 += W1[idx]
                current_W2 += W2[idx]
                current_W3 += W3[idx]

        population.append(individual)

    return population


def fitness(solution):
    # As fitness, here we have the final evalution function.
    # But you may employ more advanced fitnesses functions to help fast converge in better solutions.
    # Incorporate strategies discussed during the lectures.
    

    total_W1, total_W2, total_W3 = np.dot(solution, W1), np.dot(solution, W2), np.dot(solution, W3)
    total_V = np.dot(solution, V)

    if total_W1 < capacity1 and total_W2 < capacity2 and total_W3 < capacity3:
        return total_V
    else:
        return 0


# it is recomended to build more advanced select_parent and mutate mechanisms
def select_parent(population):
    # Tournament selection
    individual1, individual2 = random.sample(population, 2)
    if fitness(individual1) > fitness(individual2):
        return individual1
    else:
        return individual2

def repair(individual, W1, W2, W3, max_W1=500, max_W2=750, max_W3=1000):
    current_W1, current_W2, current_W3 = np.dot(individual, W1), np.dot(individual, W2), np.dot(individual, W3)

    while current_W1 > max_W1 or current_W2 > max_W2 or current_W3 > max_W3:
        # Find the item contributing the most to the excess weight and remove it
        excess_contributions = [(i, W1[i] + W2[i] + W3[i]) for i in range(len(individual)) if individual[i] == 1]
        if not excess_contributions:
            break
        worst_item = max(excess_contributions, key=lambda x: x[1])[0]
        individual[worst_item] = 0
        current_W1, current_W2, current_W3 = np.dot(individual, W1), np.dot(individual, W2), np.dot(individual, W3)

    return individual


def crossover(parent1, parent2):
    crossover_point = random.randint(1, vector_size - 1)
    child = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    return repair(child, W1, W2, W3, max_W1=500, max_W2=750, max_W3=1000)

def mutate(individual):
    for i in range(vector_size):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # flip bit
    return repair(individual, W1, W2, W3, max_W1=500, max_W2=750, max_W3=1000)


# <-------------- your main algorithm function goes here
def Algorithm():
    t_1 = time.time()
    population = initialize_population(population_size, 10000, W1, W2, W3, V, max_W1=500, max_W2=750, max_W3=1000)
    cnt = 0

    for _ in range(num_iterations):
        cnt += 1
        new_population = []

        # Elitism
        best_solution = max(population, key=fitness)
        new_population.append(best_solution)

        for _ in range(population_size - 1):  # Adjusted to maintain population size
            parent1 = select_parent(population)
            parent2 = select_parent(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

        if cnt % 5 == 0:
            best_solution = max(population, key=fitness)
            solution_value = fitness(best_solution)
            print(f"Value: {solution_value}")

        t_2 = time.time()
        if t_2 - t_1 >= 1000:
            break

    return best_solution

import numpy as np
import random

# <----------- import your approach here


np.random.seed(42)
random.seed(42)

root_folder = 'Public/'
W1 = np.load("weights1.npy")
W2 = np.load("weights2.npy")
W3 = np.load("weights3.npy")
V = np.load("values.npy")
capacity1, capacity2, capacity3 = 500, 750, 1000 # the boundary constraints for each W

# W1, W2, W3, V look like: [0.15795, 0.0086 , 0.7682 , ...  0.73664, 0.50227, 0.3245]
#                       IDS:  0        1        2      ...   9997     9998     9999  # 10000 items

# e.g. solution = [0, 1, 0, 0, 1, 1, 1, .....] # 10000 size
# "1" means: place item in the corresponding id, "0" means not place
def evaluate(solution):
    total_W1, total_W2, total_W3 = np.dot(solution, W1), np.dot(solution, W2), np.dot(solution, W3)
    total_V = np.dot(solution, V)
    if total_W1 < capacity1 and total_W2 < capacity2 and total_W3 < capacity3:
        return total_V
    else:
        return 0

#  your algorithm function goes here -------------->
solution = Algorithm()  # It must be named: "Algorithm", it takes as input the data and outputs your solution
# <----------------------
solution_value = evaluate(solution)
print(f"Final Solution Value: {solution_value}")
print("PAPOUTSAKIS ANDREAS  Multi-Constrained Knapsack Problem  Project ")

